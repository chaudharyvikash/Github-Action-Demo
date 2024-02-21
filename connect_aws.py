import logging
import boto3
import json
from botocore.exceptions import ClientError
import os

class AWSConnector():
    __instance = None

    def __new__(cls):
        if AWSConnector.__instance is None:
            AWSConnector.__instance = object.__new__(cls)
        return AWSConnector.__instance

    def connect(self):        
        client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        return client

client=AWSConnector().connect()
with open("output.json", "rb") as f:
     client.upload_fileobj(f, "cve-import", "test.json")

