import boto3, uuid, json, os, requests, time
from dotenv import load_dotenv

load_dotenv()
RIOT_API_KEY = os.getenv("RIOT_API_KEY")
PLAYER_QUEUE_URL = os.getenv("PLAYER_QUEUE_URL")
S3_BUCKET = os.getenv("S3_BUCKET")
PROGRESS_TABLE = os.getenv("PROGRESS_TABLE")
REGION_MAPPINGS = {
    "na1": "americas",
    "br1": "americas",
    "la1": "americas",
    "la2": "americas",
    "kr": "asia",
    "jp1": "asia",
    "eun1": "europe",
    "euw1": "europe",
    "me1": "europe",
    "tr1": "europe",
    "ru": "europe",
    "oc1": "sea",
    "sg2": "sea",
    "tw2": "sea",
    "vn2": "sea",
}

class AWSQueueManager:
    def __init__(self):
        self.sqs = boto3.client("sqs")
        self.s3 = boto3.client("s3")
        self.ddb = boto3.resource("dynamodb")

    # expect in input: region, gameName, tagLine
    def enqueue(self, input: dict):
        # validate input
        region = input.get("region")
        gameName = input.get("gameName")
        tagLine = input.get("tagLine")

        if not (region and gameName and tagLine):
            return {"status": 400, "message": "Bad parameters"}
        
        # get puuid given gameName and tagLine
        # also get exact character cases
        temp_routing = "asia" if REGION_MAPPINGS.get(region) == "sea" else REGION_MAPPINGS.get(region)
        header = {"X-Riot-Token": RIOT_API_KEY}
        endpoint = f"https://{temp_routing}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}"
        resp = requests.get(endpoint, headers=header)
        if resp.status_code != 200:
            return {"status": resp.status_code, "message": resp.reason}
        data = resp.json()
        puuid = data.get("puuid")
        gameName = data.get("gameName")
        tagLine = data.get("tagLine")

        # check if this player is already in table and if they are done processing
        table = self.ddb.Table(PROGRESS_TABLE)
        item_resp = table.get_item(
            Key={"user": f"{gameName}#{tagLine}"},
            ProjectionExpression="done_processing"
        )
        item = item_resp.get("Item")
        if item:
            print(f"User {gameName}#{tagLine} already in table")
            done_processing = item.get("done_processing")
            message = "Ready" if done_processing else "In progress"
            return {"status": 200, "message": message}

        # create message body
        routing = REGION_MAPPINGS.get(region)
        body = {
            "routing": routing,
            "puuid": puuid,
            "gameName": gameName,
            "tagLine": tagLine
        }
        
        # enqueue player
        self.sqs.send_message(
            QueueUrl=PLAYER_QUEUE_URL,
            MessageBody=json.dumps(body),
            MessageGroupId="player",
            MessageDeduplicationId=str(uuid.uuid4())
        )

        return {"status": 200, "message": "Player enqueued"}