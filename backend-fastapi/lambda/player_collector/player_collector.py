import os, json, boto3, requests, uuid, random, time
from datetime import datetime, timezone
#from dotenv import load_dotenv

#load_dotenv()
RIOT_API_KEY = os.getenv("RIOT_API_KEY")
MATCH_QUEUE_URL = os.getenv("MATCH_QUEUE_URL")
SQS = boto3.client("sqs")
JAN_5_2025 = int(datetime(2025, 1, 5, tzinfo=timezone.utc).timestamp())
NOV_1_2025 = int(datetime(2025, 11, 1, tzinfo=timezone.utc).timestamp())
BATCH_SIZE = 50
REQUEST_DELAY = 1.2

def lambda_handler(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])

        # need routing, puuid, gameName, tagLine
        routing = body.get("routing")
        puuid = body.get("puuid")
        gameName = body.get("gameName")
        tagLine = body.get("tagLine")

        if not (routing and puuid and gameName and tagLine):
            print("Player collector error")
            raise Exception("Error in body")
        
        # collect match ids
        print(f"Collecting all matches for {gameName}#{tagLine}")
        matchIds = get_all_match_ids(routing, puuid)
        if len(matchIds) == 0:
            print(f"No games found for {gameName}#{tagLine}")
            continue
        print(f"Got {len(matchIds)} for {gameName}#{tagLine}")

        # batch ids, send to match processing queue
        # batches processed in fifo order, but the individual matches should be done concurrently
        # only need to send routing, matchIds,
        # send gameName, tagLine for naming purposes
        num_batches_sent = 0
        for i in range(0, len(matchIds), BATCH_SIZE):
            batch = matchIds[i:i+BATCH_SIZE]
            SQS.send_message(
                QueueUrl=MATCH_QUEUE_URL,
                MessageGroupId="match",
                MessageDeduplicationId=str(uuid.uuid4()),
                MessageBody=json.dumps({
                    "routing": routing,
                    "gameName": gameName,
                    "tagLine": tagLine,
                    "matchIds": batch
                })
            )
            num_batches_sent += 1
        print(f"Enqueued {num_batches_sent} match batches for {gameName}#{tagLine}")

    return {"status": 200, "message": f"Finished processing"}

def riot_request(url, headers, params):
    for i in range(5):
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code == 429:
            print("Hit rate limit, snoozin' for a bit")
            backoff = 2 ** (i + 1) + random.uniform(0, 1)
            time.sleep(min(backoff, 15))
            continue
        resp.raise_for_status()
        return resp
    raise Exception("Rate limited")

def get_all_match_ids(routing, puuid):
    header = {"X-Riot-Token": RIOT_API_KEY}
    endpoint = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
    all_match_ids = []
    for queue in [400, 420, 430, 440, 490]:
        start = 0
        params = {
            "startTime": JAN_5_2025,
            "endTime": NOV_1_2025,
            "queue": queue,
            "start": start,
            "count": 100
        }
        while True:
            params["start"] = start
            resp = riot_request(endpoint, headers=header, params=params)
            time.sleep(REQUEST_DELAY)
            resp.raise_for_status()
            data = resp.json()
            all_match_ids.extend(data)

            if len(data) == params.get("count", 100):
                start += params.get("count", 100)
            else:
                break
    
    return all_match_ids