from pydantic import BaseModel
from typing import List, Optional, Dict, Any, Literal, Union


class Position(BaseModel):
    x: int
    y: int


class PlayerFrame(BaseModel):
    playerId: int
    position: Position
    currentGold: int
    totalGold: int
    level: int
    xp: int
    minionsKilled: int
    jungleMinionsKilled: int

    totalDamageDone: int
    totalDamageDoneToChampions: int
    totalDamageTaken: int
    physicalDamageDone: int
    physicalDamageDoneToChampions: int
    physicalDamageTaken: int
    magicDamageDone: int
    magicDamageDoneToChampions: int
    magicDamageTaken: int
    trueDamageDone: int
    trueDamageDoneToChampions: int
    trueDamageTaken: int


class PlayersFrame(BaseModel):
    playerFrames: Dict[str, PlayerFrame]  # Define PlayerFrame as needed


class VictimDamage(BaseModel):
    basic: bool
    physicalDamage: int
    magicDamage: int
    trueDamage: int
    name: str
    participantId: int
    spellName: str
    spellSlot: int
    type: str


class EventBase(BaseModel):
    type: str
    timestamp: int


class PauseEnd(EventBase):
    type: Literal["PAUSE_END"]
    realTimestamp: int


# class ItemPurchased(EventBase):
#     type: Literal["ITEM_PURCHASED"]
#     participantId: int
#     itemId: int


# class ItemUndo(EventBase):
#     type: Literal["ITEM_UNDO"]
#     participantId: int
#     beforeId: int
#     afterId: int
#     goldGain: int


# class SkillLevelUp(EventBase):
#     type: Literal["SKILL_LEVEL_UP"]
#     participantId: int
#     skillSlot: int
#     levelUpType: Optional[str]


# class ItemDestroyed(EventBase):
#     type: Literal["ITEM_DESTROYED"]
#     participantId: int
#     itemId: int


class WardPlaced(EventBase):
    type: Literal["WARD_PLACED"]
    creatorId: int
    wardType: str


class WardKill(EventBase):
    type: Literal["WARD_KILL"]
    killerId: int
    wardType: str


class LevelUp(EventBase):
    type: Literal["LEVEL_UP"]
    participantId: int
    level: int


class ChampionKill(EventBase):
    type: Literal["CHAMPION_KILL"]
    killerId: int
    victimId: int
    bounty: int
    shutdownBounty: int
    killStreakLength: int
    position: Position
    assistingParticipantIds: List[int] = []
    victimDamageDealt: List[VictimDamage] = []
    victimDamageReceived: List[VictimDamage] = []


class ChampionSpecialKill(EventBase):
    type: Literal["CHAMPION_SPECIAL_KILL"]
    killType: str
    killerId: int
    # position: Optional[Position]


class ChampionSpecialKillFirstBlood(ChampionSpecialKill):
    killType: Literal["KILL_FIRST_BLOOD"]


class ChampionSpecialKillMultiKill(ChampionSpecialKill):
    killType: Literal["KILL_MULTI"]
    multiKillLength: int


# class TurretPlateDestroyed(EventBase):
#     type: Literal["TURRET_PLATE_DESTROYED"]
#     killerId: int
#     laneType: str
#     teamId: int
#     position: Optional[Position]


class EliteMonsterKill(EventBase):
    type: Literal["ELITE_MONSTER_KILL"]
    killerId: int
    killerTeamId: int
    # bounty: Optional[int]
    monsterType: Literal["HORDE", "ATAKHAN", "DRAGON", "RIFTHERALD", "BARON_NASHOR"]
    # position: Optional[Position]
    assistingParticipantIds: List[int] = []


class DragonMonsterKill(EliteMonsterKill):
    monsterType: Literal["DRAGON"]
    monsterSubType: Literal["AIR_DRAGON", "WATER_DRAGON", "FIRE_DRAGON", "EARTH_DRAGON", "CHEMTECH_DRAGON", "HEXTECH_DRAGON", "ELDER_DRAGON", "UNKNOWN"]


class BuildingKill(EventBase):
    type: Literal["BUILDING_KILL"]
    killerId: int
    # bounty: Optional[int]
    buildingType: str
    laneType: Literal["MID_LANE", "TOP_LANE", "BOT_LANE"]
    # position: Optional[Position]
    buildingTeamId: int
    assistingParticipantIds: List[int] = []


class TowerKill(BuildingKill):
    buildingType: Literal["TOWER_BUILDING"]
    towerType: Literal["OUTER_TURRET", "INNER_TURRET", "BASE_TURRET", "NEXUS_TURRET"]


class InhibitorKill(BuildingKill):
    buildingType: Literal["INHIBITOR_BUILDING"]


# class ItemSold(EventBase):
#     type: Literal["ITEM_SOLD"]
#     participantId: int
#     itemId: int


# class ObjectiveBountyPrestart(EventBase):
#     type: Literal["OBJECTIVE_BOUNTY_PRESTART"]
#     teamId: int
#     actualStartTime: int


# class ObjectiveBountyFinish(EventBase):
#     type: Literal["OBJECTIVE_BOUNTY_FINISH"]
#     teamId: int


# class DragonSoulGiven(EventBase):
#     type: Literal["DRAGON_SOUL_GIVEN"]
#     teamId: int
#     name: str


class GameEnd(EventBase):
    type: Literal["GAME_END"]
    gameId: int
    realTimestamp: int
    winningTeam: int


# class ChampionTransform(EventBase):
#     type: Literal["CHAMPION_TRANSFORM"]
#     participantId: int
#     transformType: str


# class FeatUpdate(EventBase):
#     type: Literal["FEAT_UPDATE"]
#     teamId: int
#     featType: str
#     featValue: int


class FrameData(BaseModel):
    playersFrames: List[PlayersFrame]  # Define ParticipantFrame as needed
    events: List[
        Union[
            PauseEnd,
            # ItemPurchased,
            # ItemUndo,
            # SkillLevelUp,
            WardPlaced,
            WardKill,
            LevelUp,
            # ItemDestroyed,
            ChampionKill,
            ChampionSpecialKill,
            # TurretPlateDestroyed,
            EliteMonsterKill,
            BuildingKill,
            # ItemSold,
            # ObjectiveBountyPrestart,
            # ObjectiveBountyFinish,
            # DragonSoulGiven,
            GameEnd,
            # ChampionTransform,
            # FeatUpdate,
        ]
    ]  # Define EventData as needed


class TimelinePlayerData(BaseModel):
    playerId: int
    puuid: str


class TimelineMetadata(BaseModel):
    dataVersion: str
    matchId: str
    gameId: int
    endOfGameResult: str
    players: List[TimelinePlayerData]


class MatchTimelineData(BaseModel):
    metadata: TimelineMetadata
    frameInterval: int
    frames: List[FrameData]  # Define FrameData as needed
