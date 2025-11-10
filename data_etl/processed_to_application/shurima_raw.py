from match_model import MatchData
from timeline_model import MatchTimelineData


def get_raw_shurima_metrics_for_match(puuid: str, match_data: MatchData, timeline_data: MatchTimelineData):
    player = match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)]
    play_time = player.combat.timePlayed / 60
    team = set([p.identity.participantId for p in match_data.players if p.identity.teamId == player.identity.teamId])
    turret_kills = player.objectives.turretKills
    dragon_kills = player.objectives.dragonKills
    baron_kills = player.objectives.baronKills
    herald_kills = 0
    atakhan_kills = 0
    dragon_killed = False
    first_dragon_kill = False
    baron_killed = False
    first_baron_kill = False
    rift_herald_killed = False
    first_rift_herald_kill = False

    total_team_objectives_structures = 0
    total_team_objectives_jungle_bosses = 0
    total_player_objectives_structures_participation = 0
    total_player_objectives_jungle_bosses_participation = 0

    for frame in timeline_data.frames:
        for event in frame.events:
            if event.type == "ELITE_MONSTER_KILL":
                if event.monsterType == "RIFTHERALD":
                    if event.killerId in team:
                        total_team_objectives_jungle_bosses += 1
                        if event.killerId == player.identity.participantId or event.assistingParticipantIds and player.identity.participantId in event.assistingParticipantIds:
                            total_player_objectives_jungle_bosses_participation += 1
                    if event.killerId == player.identity.participantId:
                        herald_kills += 1
                        if rift_herald_killed is False:
                            first_rift_herald_kill = True
                    rift_herald_killed = True
                elif event.monsterType == "ATAKHAN":
                    if event.killerId in team:
                        total_team_objectives_jungle_bosses += 1
                        if event.killerId == player.identity.participantId or event.assistingParticipantIds and player.identity.participantId in event.assistingParticipantIds:
                            total_player_objectives_jungle_bosses_participation += 1
                    if event.killerId == player.identity.participantId:
                        atakhan_kills += 1
                elif event.monsterType == "DRAGON":
                    if event.killerId in team:
                        total_team_objectives_jungle_bosses += 1
                        if event.killerId == player.identity.participantId or event.assistingParticipantIds and player.identity.participantId in event.assistingParticipantIds:
                            total_player_objectives_jungle_bosses_participation += 1
                    if dragon_killed is False:
                        if event.killerId == player.identity.participantId:
                            first_dragon_kill = True
                    dragon_killed = True
                elif event.monsterType == "BARON_NASHOR":
                    if event.killerId in team:
                        total_team_objectives_jungle_bosses += 1
                        if event.killerId == player.identity.participantId or event.assistingParticipantIds and player.identity.participantId in event.assistingParticipantIds:
                            total_player_objectives_jungle_bosses_participation += 1
                    if baron_killed is False:
                        if event.killerId == player.identity.participantId:
                            first_baron_kill = True
                    baron_killed = True
            elif event.type == "BUILDING_KILL":
                if event.killerId in team:
                    total_team_objectives_structures += 1
                    if event.killerId == player.identity.participantId or event.assistingParticipantIds and player.identity.participantId in event.assistingParticipantIds:
                        total_player_objectives_structures_participation += 1

    objective_participation_ratio = (total_player_objectives_structures_participation + total_player_objectives_jungle_bosses_participation) / max(
        1, (total_team_objectives_structures + total_team_objectives_jungle_bosses)
    )
    first_tower_kill = player.objectives.firstTowerKill
    damage_dealt_to_objectives = player.objectives.damageDealtToObjectives
    damage_dealt_to_structures = player.objectives.damageDealtToBuildings + player.objectives.damageDealtToTurrets

    return {
        "play_time": play_time,
        "turret_kills": turret_kills,
        "dragon_kills": dragon_kills,
        "baron_kills": baron_kills,
        "herald_kills": herald_kills,
        "atakhan_kills": atakhan_kills,
        "first_tower_kill": first_tower_kill,
        "first_dragon_kill": first_dragon_kill,
        "first_baron_kill": first_baron_kill,
        "first_rift_herald_kill": first_rift_herald_kill,
        "objective_participation_ratio": objective_participation_ratio,
        "damage_dealt_to_objectives": damage_dealt_to_objectives,
        "damage_dealt_to_structures": damage_dealt_to_structures,
    }
