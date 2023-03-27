import datetime
import logging
from configparser import ConfigParser

import boto3
from botocore.exceptions import ClientError


class S3Client:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("gclfs.config")
        profile = self.config.get("s3", "profile", fallback="gclfs")
        boto3.setup_default_session(profile_name=profile)
        self.client = boto3.client('s3')
        self.bucket = boto3.resource('s3').Bucket(
            self.config.get("s3", "bucket"),
        )

    def presigned_url(self, base, file_name: str):
        """Create a pre-signed URL to upload to S3"""

        try:
            presigned_post = self.client.generate_presigned_post(
                self.client[self.config.get("s3", "bucket")],
                file_name,
                ExpiresIn=300
            )
        except ClientError as error:
            logging.error("Get Presigned URL", extra={
                "detail": str(error),
                "timestamp": str(datetime.datetime.now())
            })
            raise
        return presigned_post
