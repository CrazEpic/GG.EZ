import os
import boto3
from typing import List, Optional, Dict, Any, Literal, Union
import json

from match_model import (
    PlayerIdentity,
    CombatStats,
    ObjectiveStats,
    EconomyStats,
    VisionStats,
    PerkSelection,
    PerkStyle,
    Perks,
    AbilityStats,
    PingStats,
    FarmingStats,
    PlayerData,
    TeamInfo,
    GameContext,
    MatchData,
)
from timeline_model import (
    Position,
    PlayerFrame,
    PlayersFrame,
    VictimDamage,
    EventBase,
    PauseEnd,
    WardPlaced,
    WardKill,
    LevelUp,
    ChampionKill,
    ChampionSpecialKill,
    ChampionSpecialKillFirstBlood,
    ChampionSpecialKillMultiKill,
    EliteMonsterKill,
    DragonMonsterKill,
    BuildingKill,
    TowerKill,
    InhibitorKill,
    GameEnd,
    FrameData,
    TimelinePlayerData,
    TimelineMetadata,
    MatchTimelineData,
)

S3_BUCKET = os.getenv("S3_BUCKET")
S3 = boto3.client("s3")


def lambda_handler(event, context):
    puuid = event["puuid"]
    player_info = S3.get_object(
        Bucket=S3_BUCKET,
        Key=f"players/{puuid}/info.json",
    )
    player_info = json.load(player_info["Body"])
    matches = player_info["matches"]

    successfully_processed_count = 0
    error_count = 0

    matches = matches[:1]

    for match_id in matches:
        try:
            match = process_match(match_id)
            timeline = process_timeline(match_id)
            print("Processed both")
            S3.put_object(
                Bucket=S3_BUCKET,
                Key=f"processed/{match_id}/match.json",
                Body=match.model_dump_json(indent=4),
            )
            S3.put_object(
                Bucket=S3_BUCKET,
                Key=f"processed/{match_id}/timeline.json",
                Body=timeline.model_dump_json(indent=4),
            )
            successfully_processed_count += 1
        except Exception as e:
            print(f"Error processing match {match_id}: {e}")
            error_count += 1

    return {"status": 200, "message": f"Processed {successfully_processed_count} matches for {puuid}. There were {error_count} errors.", "puuid": puuid}


def process_match(match_id: str):
    match_info = S3.get_object(
        Bucket=S3_BUCKET,
        Key=f"raw/{match_id}/match.json",
    )
    data = json.loads(match_info["Body"].read().decode("utf-8"))
    match = MatchData(
        game=GameContext(
            matchId=data["metadata"]["matchId"],
            platformId=data["info"]["platformId"],
            gameId=data["info"]["gameId"],
            queueId=data["info"]["queueId"],
            mapId=data["info"]["mapId"],
            gameMode=data["info"]["gameMode"],
            gameType=data["info"]["gameType"],
            gameVersion=data["info"]["gameVersion"],
            gameName=data["info"]["gameName"],
            gameCreation=data["info"]["gameCreation"],
            gameStartTimestamp=data["info"]["gameStartTimestamp"],
            gameEndTimestamp=data["info"]["gameEndTimestamp"],
            gameDuration=data["info"]["gameDuration"],
            teams=[TeamInfo(teamId=team["teamId"], win=team["win"]) for team in data["info"]["teams"]],
            participants=[participant["puuid"] for participant in data["info"]["participants"]],
            gameEndedInSurrender=any([player["gameEndedInSurrender"] for player in data["info"]["participants"]]),
            endOfGameResult=data["info"]["endOfGameResult"],
        ),
        players=[
            PlayerData(
                identity=PlayerIdentity(
                    puuid=player["puuid"],
                    riotIdGameName=player["riotIdGameName"],
                    riotIdTagline=player["riotIdTagline"],
                    summonerName=player["summonerName"],
                    summonerId=player["summonerId"],
                    profileIcon=player["profileIcon"],
                    summonerLevel=player["summonerLevel"],
                    participantId=player["participantId"],
                    teamId=player["teamId"],
                    individualPosition=player["individualPosition"],
                    teamPosition=player["teamPosition"],
                    role=player["role"],
                    lane=player["lane"],
                    championName=player["championName"],
                    championId=player["championId"],
                    champLevel=player["champLevel"],
                    champExperience=player["champExperience"],
                ),
                combat=CombatStats(
                    kills=player["kills"],
                    deaths=player["deaths"],
                    assists=player["assists"],
                    firstBloodAssist=player["firstBloodAssist"],
                    firstBloodKill=player["firstBloodKill"],
                    doubleKills=player["doubleKills"],
                    tripleKills=player["tripleKills"],
                    quadraKills=player["quadraKills"],
                    pentaKills=player["pentaKills"],
                    unrealKills=player["unrealKills"],
                    killingSprees=player["killingSprees"],
                    largestKillingSpree=player["largestKillingSpree"],
                    largestMultiKill=player["largestMultiKill"],
                    longestTimeSpentLiving=player["longestTimeSpentLiving"],
                    totalTimeSpentDead=player["totalTimeSpentDead"],
                    timePlayed=player["timePlayed"],
                    totalDamageDealt=player["totalDamageDealt"],
                    totalDamageDealtToChampions=player["totalDamageDealtToChampions"],
                    physicalDamageDealt=player["physicalDamageDealt"],
                    physicalDamageDealtToChampions=player["physicalDamageDealtToChampions"],
                    magicDamageDealt=player["magicDamageDealt"],
                    magicDamageDealtToChampions=player["magicDamageDealtToChampions"],
                    trueDamageDealt=player["trueDamageDealt"],
                    trueDamageDealtToChampions=player["trueDamageDealtToChampions"],
                    totalDamageTaken=player["totalDamageTaken"],
                    physicalDamageTaken=player["physicalDamageTaken"],
                    magicDamageTaken=player["magicDamageTaken"],
                    trueDamageTaken=player["trueDamageTaken"],
                    damageSelfMitigated=player["damageSelfMitigated"],
                    totalHeal=player["totalHeal"],
                    totalHealsOnTeammates=player["totalHealsOnTeammates"],
                    totalDamageShieldedOnTeammates=player["totalDamageShieldedOnTeammates"],
                    timeCCingOthers=player["timeCCingOthers"],
                    totalTimeCCDealt=player["totalTimeCCDealt"],
                ),
                objectives=ObjectiveStats(
                    turretKills=player["turretKills"],
                    turretTakedowns=player["turretTakedowns"],
                    turretsLost=player["turretsLost"],
                    inhibitorKills=player["inhibitorKills"],
                    inhibitorTakedowns=player["inhibitorTakedowns"],
                    inhibitorsLost=player["inhibitorsLost"],
                    firstTowerAssist=player["firstTowerAssist"],
                    firstTowerKill=player["firstTowerKill"],
                    baronKills=player["baronKills"],
                    dragonKills=player["dragonKills"],
                    # riftHeraldKills=player["riftHeraldKills"],
                    # elderDragonKills=player["elderDragonKills"],
                    # atakhanKills=player["atakhanKills"],
                    damageDealtToBuildings=player["damageDealtToBuildings"],
                    damageDealtToTurrets=player["damageDealtToTurrets"],
                    damageDealtToObjectives=player["damageDealtToObjectives"],
                    objectivesStolen=player["objectivesStolen"],
                    objectivesStolenAssists=player["objectivesStolenAssists"],
                    nexusKills=player["nexusKills"],
                    nexusTakedowns=player["nexusTakedowns"],
                    nexusLost=player["nexusLost"],
                ),
                economy=EconomyStats(
                    goldEarned=player["goldEarned"],
                    goldSpent=player["goldSpent"],
                    itemsPurchased=player["itemsPurchased"],
                    consumablesPurchased=player["consumablesPurchased"],
                    item0=player["item0"],
                    item1=player["item1"],
                    item2=player["item2"],
                    item3=player["item3"],
                    item4=player["item4"],
                    item5=player["item5"],
                    item6=player["item6"],
                ),
                vision=VisionStats(
                    visionScore=player["visionScore"],
                    wardsPlaced=player["wardsPlaced"],
                    wardsKilled=player["wardsKilled"],
                    visionWardsBoughtInGame=player["visionWardsBoughtInGame"],
                ),
                abilityUsage=AbilityStats(
                    spell1Casts=player["spell1Casts"],
                    spell2Casts=player["spell2Casts"],
                    spell3Casts=player["spell3Casts"],
                    spell4Casts=player["spell4Casts"],
                    summoner1Id=player["summoner1Id"],
                    summoner2Id=player["summoner2Id"],
                    summoner1Casts=player["summoner1Casts"],
                    summoner2Casts=player["summoner2Casts"],
                    perks=Perks(
                        statPerks=player["perks"]["statPerks"],
                        styles=[
                            PerkStyle(
                                description=style["description"],
                                selections=[
                                    PerkSelection(
                                        perk=selection["perk"],
                                        var1=selection["var1"],
                                        var2=selection["var2"],
                                        var3=selection["var3"],
                                    )
                                    for selection in style["selections"]
                                ],
                                style=style["style"],
                            )
                            for style in player["perks"]["styles"]
                        ],
                    ),
                ),
                pings=PingStats(
                    allInPings=player["allInPings"],
                    assistMePings=player["assistMePings"],
                    basicPings=player["basicPings"],
                    commandPings=player["commandPings"],
                    dangerPings=player["dangerPings"],
                    getBackPings=player["getBackPings"],
                    holdPings=player["holdPings"],
                    onMyWayPings=player["onMyWayPings"],
                    pushPings=player["pushPings"],
                    retreatPings=player["retreatPings"],
                    needVisionPings=player["needVisionPings"],
                    enemyMissingPings=player["enemyMissingPings"],
                    enemyVisionPings=player["enemyVisionPings"],
                    visionClearedPings=player["visionClearedPings"],
                ),
                farming=FarmingStats(
                    totalMinionsKilled=player["totalMinionsKilled"],
                    neutralMinionsKilled=player["neutralMinionsKilled"],
                    totalAllyJungleMinionsKilled=player["totalAllyJungleMinionsKilled"],
                    totalEnemyJungleMinionsKilled=player["totalEnemyJungleMinionsKilled"],
                ),
            )
            for player in data["info"]["participants"]
        ],
    )
    return match


def parse_event(event: dict):
    match event["type"]:
        # --- Basic events ---
        case "PAUSE_END":
            return PauseEnd(**event)
        case "WARD_PLACED":
            return WardPlaced(**event)
        case "WARD_KILL":
            return WardKill(**event)
        case "LEVEL_UP":
            return LevelUp(**event)
        case "CHAMPION_KILL":
            return ChampionKill(**event)
        case "GAME_END":
            return GameEnd(**event)

        # --- CHAMPION_SPECIAL_KILL subtypes ---
        case "CHAMPION_SPECIAL_KILL":
            kill_type = event.get("killType")
            if kill_type == "KILL_FIRST_BLOOD":
                return ChampionSpecialKillFirstBlood(**event)
            elif kill_type == "KILL_MULTI":
                return ChampionSpecialKillMultiKill(**event)
            else:
                return ChampionSpecialKill(**event)

        # --- ELITE_MONSTER_KILL subtypes ---
        case "ELITE_MONSTER_KILL":
            if event.get("monsterType") == "DRAGON":
                return DragonMonsterKill(**event)
            else:
                return EliteMonsterKill(**event)

        # --- BUILDING_KILL subtypes ---
        case "BUILDING_KILL":
            building_type = event.get("buildingType")
            if building_type == "TOWER_BUILDING":
                return TowerKill(**event, buildingTeamId=event["teamId"])
            elif building_type == "INHIBITOR_BUILDING":
                return InhibitorKill(**event, buildingTeamId=event["teamId"])
            else:
                return BuildingKill(**event, buildingTeamId=event["teamId"])

        case _:
            return None  # Ignore unsupported or unknown types


def process_timeline(match_id: str):
    timeline_info = S3.get_object(
        Bucket=S3_BUCKET,
        Key=f"raw/{match_id}/timeline.json",
    )
    data = json.loads(timeline_info["Body"].read().decode("utf-8"))
    timeline = MatchTimelineData(
        metadata=TimelineMetadata(
            dataVersion=data["metadata"]["dataVersion"],
            matchId=data["metadata"]["matchId"],
            gameId=data["info"]["gameId"],
            endOfGameResult=data["info"]["endOfGameResult"],
            players=[
                TimelinePlayerData(
                    playerId=player["participantId"],
                    puuid=player["puuid"],
                )
                for player in data["info"]["participants"]
            ],
        ),
        frameInterval=data["info"]["frameInterval"],
        frames=[
            FrameData(
                playersFrames=[
                    PlayersFrame(
                        playerFrames={
                            player_id: PlayerFrame(
                                playerId=player_frame["participantId"],
                                position=Position(
                                    x=player_frame["position"]["x"],
                                    y=player_frame["position"]["y"],
                                ),
                                currentGold=player_frame["currentGold"],
                                totalGold=player_frame["totalGold"],
                                level=player_frame["level"],
                                xp=player_frame["xp"],
                                minionsKilled=player_frame["minionsKilled"],
                                jungleMinionsKilled=player_frame["jungleMinionsKilled"],
                                totalDamageDone=player_frame["damageStats"]["totalDamageDone"],
                                totalDamageDoneToChampions=player_frame["damageStats"]["totalDamageDoneToChampions"],
                                totalDamageTaken=player_frame["damageStats"]["totalDamageTaken"],
                                physicalDamageDone=player_frame["damageStats"]["physicalDamageDone"],
                                physicalDamageDoneToChampions=player_frame["damageStats"]["physicalDamageDoneToChampions"],
                                physicalDamageTaken=player_frame["damageStats"]["physicalDamageTaken"],
                                magicDamageDone=player_frame["damageStats"]["magicDamageDone"],
                                magicDamageDoneToChampions=player_frame["damageStats"]["magicDamageDoneToChampions"],
                                magicDamageTaken=player_frame["damageStats"]["magicDamageTaken"],
                                trueDamageDone=player_frame["damageStats"]["trueDamageDone"],
                                trueDamageDoneToChampions=player_frame["damageStats"]["trueDamageDoneToChampions"],
                                trueDamageTaken=player_frame["damageStats"]["trueDamageTaken"],
                            )
                            for player_id, player_frame in frame["participantFrames"].items()
                        }
                    )
                ],
                events=[ev for event in frame.get("events", []) if (ev := parse_event(event)) is not None],
            )
            for frame in data["info"]["frames"]
        ],
    )
    return timeline
