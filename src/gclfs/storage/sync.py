import os
import sys
from configparser import ConfigParser
from pathlib import Path

from src.gclfs.core.strings import slugify


class CloudSync:
    def __init__(self, project_root, provider, ):
        self.config = ConfigParser()
        self.config.read(str(Path(project_root, "gclfs.config")))
        self.provider = provider
        self.project_root = project_root
        if self.provider == "s3":
            self.bucket = self.config.get("s3", "bucket")

    def cloud_sync(self, project_root, method):
        """
        Iterate through files in `.gclfsattributes` and upload if checksum has changed
        :param project_root:
        :param method:
        :return:
        """
        cloud_provider = {
            "s3": self.s3_sync
        }
        cloud_provider.get(self.provider)(project_root, method)

    def s3_sync(self, project_root, method):
        includes = []
        includes_str = ""
        with open(Path(project_root, ".gitattributes"), "a+") as attr_file:
            attr_file.seek(0)
            attrs = attr_file.readlines()
            for line in attrs:
                includes.append(f'{line.split(" ")[0]}')
                includes_str = includes_str + '--include ' + f'"{line.split(" ")[0]}" '

        excludes_str = ""
        with open(Path(project_root, ".gitignore"), "a+") as ignore_file:
            ignore_file.seek(0)
            ignores = ignore_file.readlines()
            for ignore in ignores:
                if ignore.strip() not in includes:
                    excludes_str = excludes_str + '--exclude ' + f'"{ignore.split(" ")[0].strip().replace("/", "")}/*" '

        if not includes:
            sys.exit('WARNING: No files tracked. Track files with `gcl track "*.<ext>"`.')

        profile = self.config.get("s3", "profile", fallback="gclfs")
        bucket = self.config.get("s3", "bucket")

        if method == "push":
            os.system(
                f'aws s3 sync "{project_root}/" s3://{bucket}/{slugify(str(project_root).split("/")[-1])}/ --profile {profile} --exclude "*" {includes_str} {excludes_str}')
        elif method == "pull":
            os.system(
                f'aws s3 sync s3://{bucket}/{slugify(str(project_root).split("/")[-1])}/ "{project_root}/" --profile {profile} --exclude "*" {includes_str} {excludes_str}')
        else:
            raise Exception("Unknown sync method")
