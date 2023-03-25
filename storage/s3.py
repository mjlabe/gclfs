import os
import datetime
import logging

import boto3
from botocore.exceptions import ClientError


class S3Client:
    def __init__(self):
        self.client = boto3.client('s3',
                                   aws_access_key_id=os.environ.get("ACCESS_KEY"),
                                   aws_secret_access_key=os.environ.get("SECRET_KEY"),
                                   )
        s3 = boto3.resource('s3',
                            aws_access_key_id=os.environ.get("ACCESS_KEY"),
                            aws_secret_access_key=os.environ.get("SECRET_KEY"),
                            )
        self.bucket = s3.Bucket(os.environ.get("BUCKET_NAME"))

    def presigned_url(self, base, file_name: str):
        """Create a pre-signed URL to upload to S3"""

        try:
            presigned_post = self.client.generate_presigned_post(
                self.client[os.environ.get("BUCKET_NAME")],
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

