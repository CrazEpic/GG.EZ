import json, os, requests, boto3, uuid
from datetime import datetime, timezone
from copy import deepcopy
from dotenv import load_dotenv

load_dotenv()
RIOT_API_KEY = os.getenv("RIOT_API_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")
JOB_TABLE = os.getenv("JOB_TABLE")
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL")
JAN_5_2025 = int(datetime(2025, 1, 5, tzinfo=timezone.utc).timestamp())
NOV_1_2025= int(datetime(2025, 11, 1, tzinfo=timezone.utc).timestamp())

def lambda_handler(event, context):
    for record in event["Records"]:
        # get params and stuff
        body = json.loads(record["body"])
        job_id = body["job_id"]
        params = body["params"]
        job_type = params["job_type"]
        print(f"Received job type {job_type}")
        try:
            match job_type:
                case "FETCH_ACCOUNT_DATA":
                    fetch_account_data(job_id, params)
                case "FETCH_PLAYER_INFO":
                    fetch_player_info(job_id, params)
                case "FETCH_MATCHES":
                    fetch_matches(job_id, params)
                case "FETCH_MATCH_DATA":
                    fetch_match_data(job_id, params)
                case _:
                    return {"statusCode": 400, "body": json.dumps({"message": "Invalid job type"})}
        except Exception as e:
            return {"statusCode": 500, "body": json.dumps({"message": str(e)})}
        
    return {"statusCode": 200, "body": json.dumps({"message": "Records processed"})}

def fetch_account_data(job_id: str, params: dict):
    print("in fetch account data")
    # get necessary params
    routing = params.get("routing")
    gameName = params.get("gameName")
    tagLine = params.get("tagLine")

    # validate
    if not (routing and gameName and tagLine):
        raise Exception("Invalid params for fetch_account_data")

    # build and make request
    header = {"X-Riot-Token": RIOT_API_KEY}
    endpoint = f"https://{routing}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}"
    resp = requests.get(endpoint, headers=header)
    resp.raise_for_status()
    data = resp.json()

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(JOB_TABLE)
    sqs = boto3.client("sqs")

    # create new job to fetch player info
    player_info_params = deepcopy(params)
    player_info_params.update({
        "puuid": data["puuid"],
        "job_type": "FETCH_PLAYER_INFO"
    })
    player_info_job_id = str(uuid.uuid4())
    player_info_table_item = {
        "job_id": player_info_job_id,
        "params": player_info_params
    }
    print("writing to table")
    table.put_item(Item=player_info_table_item)
    print("sending to queue")
    sqs.send_message(
        QueueUrl=SQS_QUEUE_URL,
        MessageBody=json.dumps(player_info_table_item)
    )

    # create new job to fetch matches
    matches_params = deepcopy(params)
    matches_params.update({
        "puuid": data["puuid"],
        "job_type": "FETCH_MATCHES"
    })
    matches_job_id = str(uuid.uuid4())
    matches_table_item = {
        "job_id": matches_job_id,
        "params": matches_params
    }
    print("writing to table")
    table.put_item(Item=matches_table_item)
    print("sending to queue")
    sqs.send_message(
        QueueUrl=SQS_QUEUE_URL,
        MessageBody=json.dumps(matches_table_item)
    )

    # delete this job from table since its done
    table.delete_item(Key={"job_id": job_id})

    # do something here?
    return

def fetch_player_info(job_id: str, params: dict):
    print("in fetch player info")
    # get necessary params
    region = params.get("region")
    gameName = params.get("gameName")
    tagLine = params.get("tagLine")
    puuid = params.get("puuid")

    # validate
    if not (region and puuid and gameName and tagLine):
        raise Exception("Invalid params for fetch_player_info")

    # build and make request
    header = {"X-Riot-Token": RIOT_API_KEY}
    endpoint = f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-puuid/{puuid}"
    resp = requests.get(endpoint, headers=header)
    resp.raise_for_status()
    data = resp.json()

    # write to s3
    print("writing to s3")
    s3 = boto3.client("s3")
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=f"{gameName}#{tagLine}/data/raw/rank_info.json",
        Body=json.dumps(data)
    )

    # delete this job from table
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(JOB_TABLE)
    table.delete_item(Key={"job_id": job_id})

    # do something here?
    return

def fetch_matches(job_id: str, params: dict):
    print("in fetch matches")
    # get necessary params
    routing = params.get("routing")
    puuid = params.get("puuid")
    
    # validate
    if not (routing and puuid):
        raise Exception("Invalid params for fetch_matches")
    
    # collect all matches in every valid queue type
    print("collecting all matches")
    all_matches = []
    for queue in [400, 420, 430, 440, 490]:
        matches_in_queue = 0
        start = 0
        count = 100
        copied_params = deepcopy(params)
        while True:
            copied_params.update({
                "startTime": JAN_5_2025,
                "endTime": NOV_1_2025,
                "queue": queue,
                "start": start,
                "count": count
            })

            header = {"X-Riot-Token": RIOT_API_KEY}
            endpoint = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
            resp = requests.get(endpoint, headers=header, params=copied_params)
            resp.raise_for_status()
            data = resp.json()

            all_matches.extend(data)
            matches_in_queue += len(data)
            if len(data) == count:
                start += count
            else:
                print(f"Got {matches_in_queue} matches for {queue=} for {params.get("gameName")}#{params.get("tagLine")}")
                break
        print(f"Got {len(all_matches)} matches total for {params.get("gameName")}#{params.get("tagLine")}")

    # get match data for each match id collected
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(JOB_TABLE)
    sqs = boto3.client("sqs")
    queue_url = SQS_QUEUE_URL
    print("getting match data from list")
    for matchId in all_matches:
        copied_params = deepcopy(params)
        copied_params.update({
            "job_type": "FETCH_MATCH_DATA",
            "matchId": matchId
        })
        new_job_id = str(uuid.uuid4())
        match_table_item = {
            "job_id": new_job_id,
            "params": copied_params
        }
        table.put_item(Item=match_table_item)
        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(match_table_item)
        )

    # delete this job
    table.delete_item(Key={"job_id": job_id})

    # return something here?
    return

def fetch_match_data(job_id: str, params: dict):
    print("in fetch match data")
    # get necessary params
    routing = params.get("routing")
    gameName = params.get("gameName")
    tagLine = params.get("tagLine")
    matchId = params.get("matchId")

    if not (routing and gameName and tagLine and matchId):
        raise Exception("Invalid params for fetch_match_data")
    
    # build and make request for match data
    header = {"X-Riot-Token": RIOT_API_KEY}
    match_endpoint = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/{matchId}"
    resp = requests.get(match_endpoint, headers=header)
    resp.raise_for_status()
    match_data = resp.json()

    # make request for timeline data
    timeline_endpoint = f"{match_endpoint}/timeline"
    resp = requests.get(timeline_endpoint, headers=header)
    resp.raise_for_status()
    timeline_data = resp.json()

    # write data to s3
    print("writing to s3")
    s3 = boto3.client("s3")
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=f"{gameName}#{tagLine}/data/raw/match_data/{matchId}.json",
        Body=json.dumps(match_data)
    )
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=f"{gameName}#{tagLine}/data/raw/timeline/{matchId}.json",
        Body=json.dumps(timeline_data)
    )

    # delete job from table
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(JOB_TABLE)
    table.delete_item(Key={"job_id": job_id})

    # return something here?
    return