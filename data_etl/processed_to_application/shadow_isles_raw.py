from match_model import MatchData
from timeline_model import MatchTimelineData


def get_raw_shadow_isles_metrics_for_match(puuid: str, match_data: MatchData, timeline_data: MatchTimelineData):
    player = match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)]
    play_time = player.combat.timePlayed / 60
    gameMode = match_data.game.gameMode
    deaths = player.combat.deaths
    time_spent_dead = player.combat.totalTimeSpentDead / 60
    death_positions = []
    revenge_kills = 0
    latest_death_for_revenge = None
    for frame in timeline_data.frames:
        for event in frame.events:
            if event.type == "CHAMPION_KILL":
                if event.victimId == player.identity.participantId:
                    death_positions.append((event.position.x, event.position.y))
                    latest_death_for_revenge = {
                        "time": event.timestamp,
                        "killerId": event.killerId,
                    }
                if (
                    latest_death_for_revenge
                    and event.victimId == latest_death_for_revenge["killerId"]
                    and event.killerId == player.identity.participantId
                    # within 3 minutes
                    and (event.timestamp - latest_death_for_revenge["time"] <= 3 * 60 * 1000)
                ):
                    revenge_kills += 1
                    latest_death_for_revenge = None

    game_ended_in_surrender = match_data.game.gameEndedInSurrender
    return {
        "play_time": play_time,
        "game_mode": gameMode,
        "deaths": deaths,
        "time_spent_dead": time_spent_dead,
        "death_positions": death_positions,
        "revenge_kills": revenge_kills,
        "game_ended_in_surrender": game_ended_in_surrender,
    }
