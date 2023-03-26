import os
from configparser import ConfigParser


class CloudSync:
    def __init__(self, project_root, provider, ):
        self.config = ConfigParser()
        self.config.read("gclfs.config")
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
        print("upload")
        cloud_provider = {
            "s3": self.s3_sync
        }
        cloud_provider.get(self.provider)(project_root, method)

    def s3_sync(self, project_root, method):
        includes = ""
        with open(".gitattributes", "a+") as attr_file:
            attr_file.seek(0)
            attrs = attr_file.readlines()
            for line in attrs:
                includes += f"--include {line.split(' ')[0]}"

        profile = self.config.get("s3", "profile", fallback="gclfs")
        bucket = self.config.get("s3", "bucket")

        if method == "push":
            os.system(f"aws s3 sync {project_root} s3://{bucket}/ --profile {profile} {includes}")
        elif method == "pull":
            os.system(f"aws s3 sync s3://{bucket}/ {project_root}  --profile {profile} {includes}")
        else:
            raise Exception("Unknown sync method")
