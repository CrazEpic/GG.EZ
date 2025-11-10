from match_model import MatchData
from timeline_model import MatchTimelineData


def get_raw_zaun_metrics_for_match(puuid: str, match_data: MatchData, timeline_data: MatchTimelineData):
    gameCreation = match_data.game.gameCreation
    player = match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)]
    team_players = [str(p.identity.participantId) for p in match_data.players if p.identity.teamId == player.identity.teamId]
    enemy_players = [str(p.identity.participantId) for p in match_data.players if p.identity.teamId != player.identity.teamId]
    pentakills = player.combat.pentaKills
    win = match_data.game.teams[next(i for i, t in enumerate(match_data.game.teams) if t.teamId == player.identity.teamId)].win
    max_gold_deficit = 0
    for frame in timeline_data.frames:
        team_gold = 0
        enemy_team_gold = 0
        for pf in frame.playersFrames:
            # WHY DID I DO THIS IN THE ETL, TOO LATE NOW
            actual_pf = pf.playerFrames
            for participantId in actual_pf:
                if str(participantId) in team_players:
                    team_gold += actual_pf[participantId].totalGold
                elif str(participantId) in enemy_players:
                    enemy_team_gold += actual_pf[participantId].totalGold
        gold_deficit = enemy_team_gold - team_gold
        max_gold_deficit = max(max_gold_deficit, gold_deficit)
    kills = player.combat.kills
    deaths = player.combat.deaths
    damage_dealt = player.combat.totalDamageDealtToChampions
    damage_taken = player.combat.totalDamageTaken

    return {
        "gameCreation": gameCreation,
        "pentakills": pentakills,
        "max_gold_deficit": max_gold_deficit,
        "win": win,
        "kills": kills,
        "deaths": deaths,
        "damage_dealt": damage_dealt,
        "damage_taken": damage_taken,
    }
