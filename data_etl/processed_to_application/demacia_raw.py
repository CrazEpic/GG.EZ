from match_model import MatchData
from timeline_model import MatchTimelineData


def get_raw_demacia_metrics_for_match(puuid: str, match_data: MatchData, timeline_data: MatchTimelineData):
    team_id = match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)].identity.teamId
    teammates = [
        {
            "puuid": player.identity.puuid,
            "riotIdGameName": player.identity.riotIdGameName,
            "riotIdTagline": player.identity.riotIdTagline,
        }
        for player in match_data.players
        if player.identity.puuid != puuid and player.identity.teamId == team_id
    ]
    win = match_data.game.teams[next(i for i, t in enumerate(match_data.game.teams) if t.teamId == team_id)].win
    return {
        "teammates": teammates,
        "win": win,
        "gameMode": match_data.game.gameMode,
    }
