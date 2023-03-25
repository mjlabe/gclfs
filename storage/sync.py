import json
import os

from storage.s3 import S3Client


class CloudSync:
    def __init__(self, provider):
        self.provider = provider

    def cloud_sync(self):
        """
        Iterate through files in `.gclfsattributes` and upload if checksum has changed
        :param s:
        :return:
        """
        print("upload")
        cloud_provider = {
            "s": self.s3_sync
        }
        cloud_provider.get(self.provider)()

    def s3_sync(self):
        pass
