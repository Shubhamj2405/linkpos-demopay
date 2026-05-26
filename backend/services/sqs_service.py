import boto3
import os
import json

sqs = boto3.client(
    "sqs",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

QUEUE_URL = os.getenv("SQS_QUEUE_URL")

def send_whatsapp_message(data):
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(data)
    )