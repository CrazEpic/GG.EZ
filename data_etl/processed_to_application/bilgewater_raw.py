from match_model import MatchData
from timeline_model import MatchTimelineData


def get_raw_bilgewater_metrics_for_match(puuid: str, match_data: MatchData, timeline_data: MatchTimelineData):
    player = match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)]
    play_time = player.combat.timePlayed / 60
    gold_earned = player.economy.goldEarned
    jungle_minions_killed = player.farming.neutralMinionsKilled + player.farming.totalAllyJungleMinionsKilled + player.farming.totalEnemyJungleMinionsKilled
    minions_killed = player.farming.totalMinionsKilled - jungle_minions_killed
    items = [player.economy.item0, player.economy.item1, player.economy.item2, player.economy.item3, player.economy.item4, player.economy.item5, player.economy.item6]

    highest_shutdown_bounty = 0
    total_shutdown_bounty = 0
    for frame in timeline_data.frames:
        for event in frame.events:
            if event.type == "CHAMPION_KILL":
                if event.killerId == player.identity.participantId:
                    total_shutdown_bounty += event.shutdownBounty
                    highest_shutdown_bounty = max(highest_shutdown_bounty, event.shutdownBounty)
    return {
        "play_time": play_time,
        "gold_earned": gold_earned,
        "jungle_minions_killed": jungle_minions_killed,
        "minions_killed": minions_killed,
        "items": items,
        "highest_shutdown_bounty": highest_shutdown_bounty,
        "total_shutdown_bounty": total_shutdown_bounty,
    }
