import json
import os

from storage.s3 import S3Client


class CloudSync:
    def __init__(self, provider, project_root):
        self.provider = provider
        self.project_root = project_root

    def cloud_sync(self, project_root):
        """
        Iterate through files in `.gclfsattributes` and upload if checksum has changed
        :param project_root:
        :param s:
        :return:
        """
        print("upload")
        cloud_provider = {
            "s": self.s3_sync
        }
        cloud_provider.get(self.provider)()

    def s3_sync(self):
        pr = self.project_root
        s3 = S3Client()
        s3.client()
        pass
