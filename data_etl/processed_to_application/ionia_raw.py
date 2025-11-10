import numpy as np
from numpy.linalg import norm

from match_model import MatchData, PlayerData
from timeline_model import MatchTimelineData


def extract_combat_metrics(player: PlayerData, match_data: MatchData, timeline_data: MatchTimelineData):
    team_players = [p for p in match_data.players if p.identity.teamId == player.identity.teamId]

    team_kills = sum(p.combat.kills for p in team_players)
    total_team_damage = sum(p.combat.totalDamageDealtToChampions for p in team_players)

    kill_participation = (player.combat.kills + player.combat.assists) / max(1, team_kills)
    kda = (player.combat.kills + player.combat.assists) / max(1, player.combat.deaths)
    damage_per_min = player.combat.totalDamageDealtToChampions / max(1, match_data.game.gameDuration / 60)
    damage_share = player.combat.totalDamageDealtToChampions / max(1, total_team_damage)

    multi_kills = {
        "double": player.combat.doubleKills,
        "triple": player.combat.tripleKills,
        "quadra": player.combat.quadraKills,
        "penta": player.combat.pentaKills,
    }
    first_blood_kill = player.combat.firstBloodKill
    first_blood_assist = player.combat.firstBloodAssist

    # TODO: kill streaks and shutdowns
    # TODO: put survival calculations here

    return {
        "kill_participation": kill_participation,
        "kda": kda,
        "damage_per_min": damage_per_min,
        "damage_share": damage_share,
        "double_kills": multi_kills["double"],
        "triple_kills": multi_kills["triple"],
        "quadra_kills": multi_kills["quadra"],
        "penta_kills": multi_kills["penta"],
        "first_blood_kill": first_blood_kill,
        "first_blood_assist": first_blood_assist,
    }


def extract_team_contribution_metrics(player: PlayerData, match_data: MatchData, timeline_data: MatchTimelineData):
    time_played_minutes = match_data.game.gameDuration / 60
    team_players = [p for p in match_data.players if p.identity.teamId == player.identity.teamId]

    team_kills = sum(p.combat.kills for p in team_players)

    kill_participation = (player.combat.kills + player.combat.assists) / max(1, team_kills)

    heal_shield_per_min = (player.combat.totalHealsOnTeammates + player.combat.totalDamageShieldedOnTeammates) / time_played_minutes

    total_team_objectives_taken = 0
    team_objectives_participated = 0
    for frame in timeline_data.frames:
        for event in frame.events:
            if event.type == "ELITE_MONSTER_KILL":
                if hasattr(event, "killerTeamId") and event.killerTeamId == player.identity.teamId:
                    total_team_objectives_taken += 1
                    if player.identity.participantId in event.assistingParticipantIds:
                        team_objectives_participated += 1
            # elif event.type == "BUILDING_KILL":
            #     if hasattr(event, "buildingTeamId") and event.buildingTeamId != player.identity.teamId:
            #         total_team_objectives_taken += 1
            #         if player.identity.participantId in event.assistingParticipantIds:
            #             team_objectives_participated += 1
    objective_participation_ratio = team_objectives_participated / max(1, total_team_objectives_taken)

    # roaming / lane presence
    time_outside_lane = 0
    # TODO: LOOK AT EVENT DATA TO SEE IF THEY PARTICIPATED IN OBJECTIVES OUTSIDE THEIR LANE, IF SO INCREMENT time_outside_lane
    total_time = match_data.game.gameDuration / timeline_data.frameInterval
    lane = player.identity.lane
    playerId = timeline_data.metadata.players[next(i for i, p in enumerate(timeline_data.metadata.players) if p.puuid == player.identity.puuid)].playerId
    for frame in timeline_data.frames:
        pf = next((p for p in frame.playersFrames if p.playerFrames[str(playerId)]), None)
        if pf:
            position = pf.playerFrames[str(playerId)].position
            # map is 15000 x 15000
            BOT_BLUE_SIDE_LINE = ((0, 1000), (15000, 1000))
            TOP_BLUE_SIDE_LINE = ((1000, 0), (1000, 15000))
            BOT_RED_SIDE_LINE = ((14000, 15000), (14000, 0))
            TOP_RED_SIDE_LINE = ((15000, 14000), (0, 14000))
            MID_LINE = ((0, 0), (15000, 15000))
            distance_threshold = 1000

            def point_line_distance(point, line_start, line_end):
                point = np.array(point)
                p1 = np.array(line_start)
                p2 = np.array(line_end)
                d = norm(np.cross(p2 - p1, p1 - point)) / norm(p2 - p1)
                return d

            if lane == "TOP":
                dist1 = point_line_distance((position.x, position.y), TOP_BLUE_SIDE_LINE[0], TOP_BLUE_SIDE_LINE[1])
                dist2 = point_line_distance((position.x, position.y), TOP_RED_SIDE_LINE[0], TOP_RED_SIDE_LINE[1])
                if min(dist1, dist2) > distance_threshold:
                    time_outside_lane += 1
            elif lane == "MID":
                dist = point_line_distance((position.x, position.y), MID_LINE[0], MID_LINE[1])
                if dist > distance_threshold:
                    time_outside_lane += 1
            elif lane == "BOT":
                dist1 = point_line_distance((position.x, position.y), BOT_BLUE_SIDE_LINE[0], BOT_BLUE_SIDE_LINE[1])
                dist2 = point_line_distance((position.x, position.y), BOT_RED_SIDE_LINE[0], BOT_RED_SIDE_LINE[1])
                if min(dist1, dist2) > distance_threshold:
                    time_outside_lane += 1
            elif lane == "JUNGLE":
                distance_to_top = min(
                    point_line_distance((position.x, position.y), TOP_BLUE_SIDE_LINE[0], TOP_BLUE_SIDE_LINE[1]),
                    point_line_distance((position.x, position.y), TOP_RED_SIDE_LINE[0], TOP_RED_SIDE_LINE[1]),
                )
                distance_to_bot = min(
                    point_line_distance((position.x, position.y), BOT_BLUE_SIDE_LINE[0], BOT_BLUE_SIDE_LINE[1]),
                    point_line_distance((position.x, position.y), BOT_RED_SIDE_LINE[0], BOT_RED_SIDE_LINE[1]),
                )
                distance_to_mid = point_line_distance((position.x, position.y), MID_LINE[0], MID_LINE[1])
                if min(distance_to_top, distance_to_bot, distance_to_mid) < distance_threshold:
                    time_outside_lane += 1
            total_time += 1

    roaming_ratio = time_outside_lane / max(1, total_time)

    return {
        "kill_participation": kill_participation,
        "heal_shield_per_min": heal_shield_per_min,
        "objective_participation_ratio": objective_participation_ratio,
        "roaming_ratio": roaming_ratio,
    }


def extract_resource_efficiency_metrics(player: PlayerData, match_data: MatchData, timeline_data: MatchTimelineData):
    time_played_minutes = match_data.game.gameDuration / 60

    gold_per_min = player.economy.goldEarned / max(1, time_played_minutes)
    cs_per_min = (player.farming.totalMinionsKilled + player.farming.neutralMinionsKilled + player.farming.totalAllyJungleMinionsKilled + player.farming.totalEnemyJungleMinionsKilled) / max(
        1, time_played_minutes
    )

    return {
        "gold_per_min": gold_per_min,
        "cs_per_min": cs_per_min,
    }


def extract_vision_awareness_metrics(player: PlayerData, match_data: MatchData, timeline_data: MatchTimelineData):
    time_played_minutes = match_data.game.gameDuration / 60

    vision_score_per_min = player.vision.visionScore / max(1, time_played_minutes)

    return {
        "vision_score_per_min": vision_score_per_min,
    }


def get_raw_ionia_metrics_for_match(puuid: str, match_data: MatchData, timeline_data: MatchTimelineData):
    player_data = next((player for player in match_data.players if player.identity.puuid == puuid), None)
    if player_data is None:
        return None

    lane = player_data.identity.lane
    if lane == "BOTTOM":
        lane = "ADC" if player_data.identity.role != "SUPPORT" else "SUPPORT"
    return {
        "combat_metrics": extract_combat_metrics(player_data, match_data, timeline_data),
        "team_contribution_metrics": extract_team_contribution_metrics(player_data, match_data, timeline_data),
        "resource_efficiency_metrics": extract_resource_efficiency_metrics(player_data, match_data, timeline_data),
        "vision_awareness_metrics": extract_vision_awareness_metrics(player_data, match_data, timeline_data),
        "lane": lane,
    }
