import os
import boto3
import json

from match_model import MatchData
from timeline_model import MatchTimelineData

from ionia import info_from_raw_ionia_metrics
from ionia_raw import get_raw_ionia_metrics_for_match
from demacia import info_from_raw_demacia_metrics
from demacia_raw import get_raw_demacia_metrics_for_match
from targon import info_from_raw_targon_metrics
from targon_raw import get_raw_targon_metrics_for_match
from piltover import info_from_raw_piltover_metrics
from piltover_raw import get_raw_piltover_metrics_for_match
from zaun import info_from_raw_zaun_metrics
from zaun_raw import get_raw_zaun_metrics_for_match
from bilgewater import info_from_raw_bilgewater_metrics
from bilgewater_raw import get_raw_bilgewater_metrics_for_match
from shadow_isles import info_from_raw_shadow_isles_metrics
from shadow_isles_raw import get_raw_shadow_isles_metrics_for_match
from shurima import info_from_raw_shurima_metrics
from shurima_raw import get_raw_shurima_metrics_for_match
from ixtal import info_from_raw_ixtal_metrics
from ixtal_raw import get_raw_ixtal_metrics_for_match
from noxus import info_from_raw_noxus_metrics
from noxus_raw import get_raw_noxus_metrics_for_match
from freljord import info_from_raw_freljord_metrics
from freljord_raw import get_raw_freljord_metrics_for_match

S3_BUCKET = os.getenv("S3_BUCKET")
S3 = boto3.client("s3")


def lambda_handler(event, context):
    puuid = event["puuid"]
    player_info = S3.get_object(
        Bucket=S3_BUCKET,
        Key=f"players/{puuid}/info.json",
    )
    player_info = json.load(player_info["Body"])
    matches = player_info["matches"]

    matches_counted_sr = 0
    raw_ionia_metrics_sr = []
    raw_demacia_metrics_sr = []
    raw_targon_metrics_sr = []
    raw_piltover_metrics_sr = []
    raw_zaun_metrics_sr = []
    raw_bilgewater_metrics_sr = []
    raw_shadow_isles_metrics_sr = []
    raw_shurima_metrics_sr = []
    raw_ixtal_metrics_sr = []
    raw_noxus_metrics_sr = []
    raw_freljord_metrics_sr = []

    matches_counted_aram = 0
    # raw_ionia_metrics_aram = []
    raw_demacia_metrics_aram = []
    # raw_targon_metrics_aram = []
    raw_piltover_metrics_aram = []
    raw_zaun_metrics_aram = []
    raw_bilgewater_metrics_aram = []
    raw_shadow_isles_metrics_aram = []
    # raw_shurima_metrics_aram = []
    # raw_ixtal_metrics_aram = []
    raw_noxus_metrics_aram = []
    raw_freljord_metrics_aram = []

    play_time_sr = 0
    play_time_aram = 0
    wins_sr = 0
    wins_aram = 0

    successfully_processed_count = 0
    error_count = 0

    for match_id in matches:
        try:
            match_obj = S3.get_object(
                Bucket=S3_BUCKET,
                Key=f"processed/{match_id}/match.json",
            )
            match_data = MatchData.model_validate_json(match_obj["Body"].read().decode("utf-8"))
            timeline_obj = S3.get_object(
                Bucket=S3_BUCKET,
                Key=f"processed/{match_id}/timeline.json",
            )
            timeline_data = MatchTimelineData.model_validate_json(timeline_obj["Body"].read().decode("utf-8"))
            gameMode = match_data.game.gameMode
            if gameMode == "CLASSIC" or gameMode == "SWIFTPLAY":
                play_time_sr += match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)].combat.timePlayed / 60
                team_id = match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)].identity.teamId
                if match_data.game.teams[next(i for i, t in enumerate(match_data.game.teams) if t.teamId == team_id)].win:
                    wins_sr += 1
                raw_ionia_metrics_sr.append(get_raw_ionia_metrics_for_match(puuid, match_data, timeline_data))
                raw_demacia_metrics_sr.append(get_raw_demacia_metrics_for_match(puuid, match_data, timeline_data))
                raw_targon_metrics_sr.append(get_raw_targon_metrics_for_match(puuid, match_data, timeline_data))
                raw_piltover_metrics_sr.append(get_raw_piltover_metrics_for_match(puuid, match_data, timeline_data))
                raw_zaun_metrics_sr.append(get_raw_zaun_metrics_for_match(puuid, match_data, timeline_data))
                raw_bilgewater_metrics_sr.append(get_raw_bilgewater_metrics_for_match(puuid, match_data, timeline_data))
                raw_shadow_isles_metrics_sr.append(get_raw_shadow_isles_metrics_for_match(puuid, match_data, timeline_data))
                raw_shurima_metrics_sr.append(get_raw_shurima_metrics_for_match(puuid, match_data, timeline_data))
                raw_ixtal_metrics_sr.append(get_raw_ixtal_metrics_for_match(puuid, match_data, timeline_data))
                raw_noxus_metrics_sr.append(get_raw_noxus_metrics_for_match(puuid, match_data, timeline_data))
                raw_freljord_metrics_sr.append(get_raw_freljord_metrics_for_match(puuid, match_data, timeline_data))
                matches_counted_sr += 1
            elif gameMode == "ARAM":
                play_time_aram += match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)].combat.timePlayed / 60
                team_id = match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)].identity.teamId
                if match_data.game.teams[next(i for i, t in enumerate(match_data.game.teams) if t.teamId == team_id)].win:
                    wins_aram += 1
                # raw_ionia_metrics_aram.append(get_raw_ionia_metrics_for_match(puuid, match_data, timeline_data))
                raw_demacia_metrics_aram.append(get_raw_demacia_metrics_for_match(puuid, match_data, timeline_data))
                # raw_targon_metrics_aram.append(get_raw_targon_metrics_for_match(puuid, match_data, timeline_data))
                raw_piltover_metrics_aram.append(get_raw_piltover_metrics_for_match(puuid, match_data, timeline_data))
                raw_zaun_metrics_aram.append(get_raw_zaun_metrics_for_match(puuid, match_data, timeline_data))
                raw_bilgewater_metrics_aram.append(get_raw_bilgewater_metrics_for_match(puuid, match_data, timeline_data))
                raw_shadow_isles_metrics_aram.append(get_raw_shadow_isles_metrics_for_match(puuid, match_data, timeline_data))
                # raw_shurima_metrics_aram.append(get_raw_shurima_metrics_for_match(puuid, match_data, timeline_data))
                # raw_ixtal_metrics_aram.append(get_raw_ixtal_metrics_for_match(puuid, match_data, timeline_data))
                raw_noxus_metrics_aram.append(get_raw_noxus_metrics_for_match(puuid, match_data, timeline_data))
                raw_freljord_metrics_aram.append(get_raw_freljord_metrics_for_match(puuid, match_data, timeline_data))
                matches_counted_aram += 1
            successfully_processed_count += 1
        except Exception as e:
            print(f"Error processing match {match_id} for player {puuid}: {e}")
            error_count += 1
            continue

    # summarize SR
    ionia_info_sr = info_from_raw_ionia_metrics(raw_ionia_metrics_sr)
    demacia_info_sr = info_from_raw_demacia_metrics(raw_demacia_metrics_sr)
    targon_info_sr = info_from_raw_targon_metrics(raw_targon_metrics_sr)
    piltover_info_sr = info_from_raw_piltover_metrics(raw_piltover_metrics_sr)
    zaun_info_sr = info_from_raw_zaun_metrics(raw_zaun_metrics_sr)
    bilgewater_info_sr = info_from_raw_bilgewater_metrics(raw_bilgewater_metrics_sr)
    shadow_isles_info_sr = info_from_raw_shadow_isles_metrics(raw_shadow_isles_metrics_sr)
    shurima_info_sr = info_from_raw_shurima_metrics(raw_shurima_metrics_sr)
    ixtal_info_sr = info_from_raw_ixtal_metrics(raw_ixtal_metrics_sr)
    noxus_info_sr = info_from_raw_noxus_metrics(raw_noxus_metrics_sr)
    freljord_info_sr = info_from_raw_freljord_metrics(raw_freljord_metrics_sr)
    # summarize ARAM
    # ionia_info_aram = info_from_raw_ionia_metrics(raw_ionia_metrics_aram)
    demacia_info_aram = info_from_raw_demacia_metrics(raw_demacia_metrics_aram)
    # targon_info_aram = info_from_raw_targon_metrics(raw_targon_metrics_aram)
    piltover_info_aram = info_from_raw_piltover_metrics(raw_piltover_metrics_aram)
    zaun_info_aram = info_from_raw_zaun_metrics(raw_zaun_metrics_aram)
    bilgewater_info_aram = info_from_raw_bilgewater_metrics(raw_bilgewater_metrics_aram)
    shadow_isles_info_aram = info_from_raw_shadow_isles_metrics(raw_shadow_isles_metrics_aram)
    # shurima_info_aram = info_from_raw_shurima_metrics(raw_shurima_metrics_aram)
    # ixtal_info_aram = info_from_raw_ixtal_metrics(raw_ixtal_metrics_aram)
    noxus_info_aram = info_from_raw_noxus_metrics(raw_noxus_metrics_aram)
    freljord_info_aram = info_from_raw_freljord_metrics(raw_freljord_metrics_aram)

    player_application_data = {
        "sr": {
            "ionia_info": ionia_info_sr,
            "demacia_info": demacia_info_sr,
            "targon_info": targon_info_sr,
            "piltover_info": piltover_info_sr,
            "zaun_info": zaun_info_sr,
            "bilgewater_info": bilgewater_info_sr,
            "shadow_isles_info": shadow_isles_info_sr,
            "shurima_info": shurima_info_sr,
            "ixtal_info": ixtal_info_sr,
            "noxus_info": noxus_info_sr,
            "freljord_info": freljord_info_sr,
        },
        "aram": {
            # "ionia_info": ionia_info_aram,
            "demacia_info": demacia_info_aram,
            # "targon_info": targon_info_aram,
            "piltover_info": piltover_info_aram,
            "zaun_info": zaun_info_aram,
            "bilgewater_info": bilgewater_info_aram,
            "shadow_isles_info": shadow_isles_info_aram,
            # "shurima_info": shurima_info_aram,
            # "ixtal_info": ixtal_info_aram,
            "noxus_info": noxus_info_aram,
            "freljord_info": freljord_info_aram,
        },
        "overview": {
            "matches_counted_sr": matches_counted_sr,
            "matches_counted_aram": matches_counted_aram,
            "play_time_sr": play_time_sr,
            "play_time_aram": play_time_aram,
            "wins_sr": wins_sr,
            "wins_aram": wins_aram,
        },
    }

    S3.put_object(
        Bucket=S3_BUCKET,
        Key=f"application/{puuid}/application_stats.json",
        Body=json.dumps(player_application_data),
    )

    return {"status": 200, "message": f"Processed -> Application. Processed {successfully_processed_count} matches for {puuid}. There were {error_count} errors."}
