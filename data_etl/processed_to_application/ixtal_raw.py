from match_model import MatchData
from timeline_model import MatchTimelineData


def get_raw_ixtal_metrics_for_match(puuid: str, match_data: MatchData, timeline_data: MatchTimelineData):
    player = match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)]
    play_time = player.combat.timePlayed / 60

    vision_score_per_min = player.vision.visionScore / max(1, play_time)
    allInPings = player.pings.allInPings
    assistMePings = player.pings.assistMePings
    basicPings = player.pings.basicPings
    commandPings = player.pings.commandPings
    dangerPings = player.pings.dangerPings
    getBackPings = player.pings.getBackPings
    holdPings = player.pings.holdPings
    onMyWayPings = player.pings.onMyWayPings
    pushPings = player.pings.pushPings
    retreatPings = player.pings.retreatPings
    needVisionPings = player.pings.needVisionPings
    enemyMissingPings = player.pings.enemyMissingPings
    enemyVisionPings = player.pings.enemyVisionPings
    visionClearedPings = player.pings.visionClearedPings

    objectives_stolen = player.objectives.objectivesStolen

    avg_jungle_share_when_jungle = "N/A"
    jungle_role = player.identity.lane == "JUNGLE"
    # TODO: maybe tailor for invade instead
    if jungle_role:
        other_jungle = next((p for p in match_data.players if p.identity.lane == "JUNGLE" and p.identity.participantId != player.identity.participantId), None)
        if other_jungle is not None:
            player_jungle_minions = player.farming.neutralMinionsKilled + player.farming.totalAllyJungleMinionsKilled + player.farming.totalEnemyJungleMinionsKilled
            other_total_jungle_minions = other_jungle.farming.neutralMinionsKilled + other_jungle.farming.totalAllyJungleMinionsKilled + other_jungle.farming.totalEnemyJungleMinionsKilled
            avg_jungle_share_when_jungle = player_jungle_minions / max(1, player_jungle_minions + other_total_jungle_minions)
        else:
            avg_jungle_share_when_jungle = 1.0

    total_wards_placed = player.vision.wardsPlaced
    total_wards_killed = player.vision.wardsKilled

    return {
        "play_time": play_time,
        "vision_score_per_min": vision_score_per_min,
        "allInPings": allInPings,
        "assistMePings": assistMePings,
        "basicPings": basicPings,
        "commandPings": commandPings,
        "dangerPings": dangerPings,
        "getBackPings": getBackPings,
        "holdPings": holdPings,
        "onMyWayPings": onMyWayPings,
        "pushPings": pushPings,
        "retreatPings": retreatPings,
        "needVisionPings": needVisionPings,
        "enemyMissingPings": enemyMissingPings,
        "enemyVisionPings": enemyVisionPings,
        "visionClearedPings": visionClearedPings,
        "objectives_stolen": objectives_stolen,
        "jungle_role": jungle_role,
        "avg_jungle_share_when_jungle": avg_jungle_share_when_jungle,
        "total_wards_placed": total_wards_placed,
        "total_wards_killed": total_wards_killed,
    }
