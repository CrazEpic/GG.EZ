import boto3, uuid, json, os
from dotenv import load_dotenv

load_dotenv()
JOB_TABLE = os.getenv("JOB_TABLE")
QUEUE_URL = os.getenv("SQS_QUEUE_URL")

class AWSQueueManager:
    def __init__(self, table_name: str=JOB_TABLE, queue_url: str=QUEUE_URL):
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(table_name)
        self.sqs = boto3.client("sqs")
        self.queue_url = queue_url

    def enqueue(self, input: dict):
        # build table job item
        job_id = str(uuid.uuid4())
        table_item = {
            "job_id": job_id,
            "params": input
        }

        # save job to table
        self.table.put_item(Item=table_item)

        # send job to queue
        self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageBody=json.dumps(table_item)
        )

        return job_id