from typing import Any, Dict, List


def info_from_raw_demacia_metrics(raw_metrics: List[Dict[str, Any]]):
    # find top 10 teammates and winrate
    teammates = {}
    for m in raw_metrics:
        for teammate in m["teammates"]:
            if teammate["puuid"] not in teammates:
                teammates[teammate["puuid"]] = {
                    "puuid": teammate["puuid"],
                    "matches": 0,
                    "wins": 0,
                    "riotIdGameName": teammate["riotIdGameName"],
                    "riotIdTagline": teammate["riotIdTagline"],
                }
            teammates[teammate["puuid"]]["matches"] += 1
            if m["win"]:
                teammates[teammate["puuid"]]["wins"] += 1
    most_common_teammates = sorted(teammates.items(), key=lambda x: x[1]["matches"], reverse=True)[:10]
    return {
        "most_common_teammates": [
            {
                "puuid": data["puuid"],
                "riotIdGameName": data["riotIdGameName"],
                "riotIdTagline": data["riotIdTagline"],
                "matches": data["matches"],
                "wins": data["wins"],
            }
            for teammate, data in most_common_teammates
        ],
    }
