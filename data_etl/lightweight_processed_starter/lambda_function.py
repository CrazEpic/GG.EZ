import json
import os
from boto3.dynamodb.types import TypeDeserializer
import boto3
import uuid

deserializer = TypeDeserializer()
client = boto3.client('stepfunctions')
STEP_ETL_ARN = os.getenv("STEP_ETL_ARN")
STEP_ETL_NAME = os.getenv("STEP_ETL_NAME")


def lambda_handler(event, context):
    etl_started = False
    for record in event["Records"]:
        if record["eventName"] != "MODIFY":
            continue
        old_image = record["dynamodb"].get("OldImage")
        new_image = record["dynamodb"].get("NewImage")
        if not old_image or not new_image:
            continue

        # Convert DynamoDB types -> normal Python types
        old_item = {k: deserializer.deserialize(v) for k, v in old_image.items()}
        new_item = {k: deserializer.deserialize(v) for k, v in new_image.items()}

        old_done = old_item.get("done_processing")
        new_done = new_item.get("done_processing")

        if old_done is False and new_done is True:
            keys = record["dynamodb"]["Keys"]
            # puuid
            puuid_attr = keys.get("puuid")

            if not puuid_attr:
                print("No puuid key in record:", keys)
                continue

            puuid = deserializer.deserialize(puuid_attr)


            unique_id = str(uuid.uuid4())

            client.start_execution(
                stateMachineArn=STEP_ETL_ARN,
                name=f"{STEP_ETL_NAME}-{unique_id[:35]}",  # unique execution name
                input=json.dumps({"puuid": puuid})
            )
            etl_started = True
    if etl_started:
        return {"statusCode": 200, "body": "ETL Started"}        

    return {"statusCode": 204, "body": "No ETL Triggered"}