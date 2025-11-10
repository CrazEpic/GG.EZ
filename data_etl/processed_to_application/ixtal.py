from typing import Any, Dict, List


def info_from_raw_ixtal_metrics(raw_metrics: List[Dict[str, Any]]):
    total_play_time = 0
    total_vision_score_per_min = 0
    total_allInPings = 0
    total_assistMePings = 0
    total_basicPings = 0
    total_commandPings = 0
    total_dangerPings = 0
    total_getBackPings = 0
    total_holdPings = 0
    total_onMyWayPings = 0
    total_pushPings = 0
    total_retreatPings = 0
    total_needVisionPings = 0
    total_enemyMissingPings = 0
    total_enemyVisionPings = 0
    total_visionClearedPings = 0
    total_objectives_stolen = 0
    total_jungle_games = 0
    total_avg_jungle_share_when_jungle = 0
    total_wards_placed = 0
    total_wards_killed = 0

    for m in raw_metrics:
        total_play_time += m["play_time"]
        total_vision_score_per_min += m["vision_score_per_min"]
        total_allInPings += m["allInPings"]
        total_assistMePings += m["assistMePings"]
        total_basicPings += m["basicPings"]
        total_commandPings += m["commandPings"]
        total_dangerPings += m["dangerPings"]
        total_getBackPings += m["getBackPings"]
        total_holdPings += m["holdPings"]
        total_onMyWayPings += m["onMyWayPings"]
        total_pushPings += m["pushPings"]
        total_retreatPings += m["retreatPings"]
        total_needVisionPings += m["needVisionPings"]
        total_enemyMissingPings += m["enemyMissingPings"]
        total_enemyVisionPings += m["enemyVisionPings"]
        total_visionClearedPings += m["visionClearedPings"]
        total_objectives_stolen += m["objectives_stolen"]
        if m["jungle_role"]:
            total_jungle_games += 1
            total_avg_jungle_share_when_jungle += m["avg_jungle_share_when_jungle"]
        total_wards_placed += m["total_wards_placed"]
        total_wards_killed += m["total_wards_killed"]
    avg_vision_score_per_min = total_vision_score_per_min / max(1, len(raw_metrics))
    avg_jungle_share_when_jungle = total_avg_jungle_share_when_jungle / max(1, total_jungle_games)

    return {
        "total_allInPings": total_allInPings,
        "total_assistMePings": total_assistMePings,
        "total_basicPings": total_basicPings,
        "total_commandPings": total_commandPings,
        "total_dangerPings": total_dangerPings,
        "total_getBackPings": total_getBackPings,
        "total_holdPings": total_holdPings,
        "total_onMyWayPings": total_onMyWayPings,
        "total_pushPings": total_pushPings,
        "total_retreatPings": total_retreatPings,
        "total_needVisionPings": total_needVisionPings,
        "total_enemyMissingPings": total_enemyMissingPings,
        "total_enemyVisionPings": total_enemyVisionPings,
        "total_visionClearedPings": total_visionClearedPings,
        "total_objectives_stolen": total_objectives_stolen,
        "avg_vision_score_per_min": avg_vision_score_per_min,
        "avg_jungle_share_when_jungle": avg_jungle_share_when_jungle,
        "total_total_wards_placed": total_wards_placed,
        "total_total_wards_killed": total_wards_killed,
    }
