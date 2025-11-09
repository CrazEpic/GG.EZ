import os, json, asyncio, aiohttp, boto3, random
from asyncio import Semaphore
#from dotenv import load_dotenv

#load_dotenv()
S3_BUCKET = os.getenv("S3_BUCKET")
RIOT_API_KEY = os.getenv("RIOT_API_KEY")
PROGRESS_TABLE = os.getenv("PROGRESS_TABLE")
S3 = boto3.client("s3")
DDB = boto3.resource("dynamodb")
CONCURRENCY = 1 # i think its a 1:1.2 ratio here with request delay idk
REQUEST_DELAY = 1.2 # 100 requests per 2 minutes in the long run

def lambda_handler(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])

        # need routing, matchIds, gameName, tagLine
        routing = body.get("routing")
        matchIds = body.get("matchIds")
        gameName = body.get("gameName")
        tagLine = body.get("tagLine")

        print(f"Processing {len(matchIds)} for {gameName}#{tagLine}")
        asyncio.run(process_batch(routing, matchIds, gameName, tagLine))
        print(f"Finished processing a batch for {gameName}#{tagLine}")

    return {"status": 200, "message": "Batch processed"}

async def riot_request(session, endpoint, headers, attempt=0):
    async with session.get(endpoint, headers=headers) as resp:
        if resp.status == 429:
            print("Hit rate limit, snoozin' for a bit")
            backoff = 2 ** attempt + random.uniform(0, 1)
            await asyncio.sleep(min(backoff, 15))
            if attempt < 5:
                return await riot_request(session, endpoint, headers, attempt=attempt + 1)
            raise Exception("Rate limited on match data fetching")
        resp.raise_for_status()
        return await resp.json()

async def process_batch(routing, matchIds, gameName, tagLine):
    semaphore = Semaphore(CONCURRENCY) # medicine
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_match(session, routing, matchId, gameName, tagLine, semaphore) for matchId in matchIds]
        await asyncio.gather(*tasks)

async def fetch_match(session, routing, matchId, gameName, tagLine, semaphore):
    header = {"X-Riot-Token": RIOT_API_KEY}
    match_endpoint = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/{matchId}"
    timeline_endpoint = f"{match_endpoint}/timeline"

    try:
        async with semaphore:
            match_task = riot_request(session, match_endpoint, headers=header)
            timeline_task = riot_request(session, timeline_endpoint, headers=header)
            match_data, timeline_data = await asyncio.gather(match_task, timeline_task)
            await asyncio.sleep(REQUEST_DELAY * 2 + random.uniform(0, 1)) # account for two requests, add some change

            S3.put_object(
                Bucket=S3_BUCKET,
                Key=f"{gameName}#{tagLine}/data/raw/match_data/{matchId}.json",
                Body=json.dumps(match_data)
            )
            S3.put_object(
                Bucket=S3_BUCKET,
                Key=f"{gameName}#{tagLine}/data/raw/timeline_data/{matchId}.json",
                Body=json.dumps(timeline_data)
            )

            table = DDB.Table(PROGRESS_TABLE)
            resp = table.update_item(
                Key={"user": f"{gameName}#{tagLine}"},
                UpdateExpression="SET processed_matches = processed_matches + :inc",
                ExpressionAttributeValues={":inc": 1},
                ReturnValues="ALL_NEW"
            )

            updated = resp["Attributes"]
            if updated["processed_matches"] >= updated["total_matches"]:
                print(f"All matches for {gameName}#{tagLine} finished")
                table.update_item(
                    Key={"user": f"{gameName}#{tagLine}"},
                    UpdateExpression="SET done_processing = :true",
                    ExpressionAttributeValues={":true": True}
                )

            print(f"Processed {matchId}")
    except Exception as e:
        print(f"Failed on {matchId}: {e}")