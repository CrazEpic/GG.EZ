from match_model import MatchData
from timeline_model import MatchTimelineData


def get_raw_piltover_metrics_for_match(puuid: str, match_data: MatchData, timeline_data: MatchTimelineData):
    gameCreation = match_data.game.gameCreation
    player = match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)]
    kda = (player.combat.kills + player.combat.assists) / max(1, player.combat.deaths)
    gold_earned = player.economy.goldEarned

    team_players = [p for p in match_data.players if p.identity.teamId == player.identity.teamId]
    team_kills = sum(p.combat.kills for p in team_players)
    kill_participation = (player.combat.kills + player.combat.assists) / max(1, team_kills)

    total_team_objectives_taken = 0
    team_objectives_participated = 0
    for frame in timeline_data.frames:
        for event in frame.events:
            if event.type == "ELITE_MONSTER_KILL":
                if hasattr(event, "killerTeamId") and event.killerTeamId == player.identity.teamId:
                    total_team_objectives_taken += 1
                    if player.identity.participantId in event.assistingParticipantIds:
                        team_objectives_participated += 1
    objective_participation_ratio = team_objectives_participated / max(1, total_team_objectives_taken)
    vision_score = player.vision.visionScore
    win = match_data.game.teams[next(i for i, t in enumerate(match_data.game.teams) if t.teamId == player.identity.teamId)].win
    return {
        "gameCreation": gameCreation,
        "kda": kda,
        "gold_earned": gold_earned,
        "kill_participation": kill_participation,
        "objective_participation_ratio": objective_participation_ratio,
        "vision_score": vision_score,
        "win": win,
    }
