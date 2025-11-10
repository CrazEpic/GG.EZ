from pydantic import BaseModel
from typing import List, Optional, Dict, Any, Literal, Union


class PlayerIdentity(BaseModel):
    puuid: str
    riotIdGameName: str
    riotIdTagline: str
    summonerName: str
    summonerId: str

    profileIcon: int
    summonerLevel: int

    participantId: int
    teamId: int
    individualPosition: str
    teamPosition: str
    role: str
    lane: str

    championName: str
    championId: int
    champLevel: int
    champExperience: int


class CombatStats(BaseModel):
    kills: int
    deaths: int
    assists: int

    firstBloodAssist: bool
    firstBloodKill: bool

    doubleKills: int
    tripleKills: int
    quadraKills: int
    pentaKills: int
    unrealKills: int

    killingSprees: int
    largestKillingSpree: int
    largestMultiKill: int

    longestTimeSpentLiving: int
    totalTimeSpentDead: int
    timePlayed: int

    totalDamageDealt: int
    totalDamageDealtToChampions: int
    physicalDamageDealt: int
    physicalDamageDealtToChampions: int
    magicDamageDealt: int
    magicDamageDealtToChampions: int
    trueDamageDealt: int
    trueDamageDealtToChampions: int

    totalDamageTaken: int
    physicalDamageTaken: int
    magicDamageTaken: int
    trueDamageTaken: int
    damageSelfMitigated: int

    totalHeal: int
    totalHealsOnTeammates: int
    totalDamageShieldedOnTeammates: int

    timeCCingOthers: int
    totalTimeCCDealt: int


class ObjectiveStats(BaseModel):
    turretKills: int
    turretTakedowns: int
    turretsLost: int
    inhibitorKills: int
    inhibitorTakedowns: int
    inhibitorsLost: int

    firstTowerAssist: bool
    firstTowerKill: bool

    baronKills: int
    dragonKills: int
    # riftHeraldKills: int
    # elderDragonKills: int
    # atakhanKills: int

    damageDealtToBuildings: int
    damageDealtToTurrets: int
    damageDealtToObjectives: int

    objectivesStolen: int
    objectivesStolenAssists: int

    nexusKills: int
    nexusTakedowns: int
    nexusLost: int


class EconomyStats(BaseModel):
    goldEarned: int
    goldSpent: int

    itemsPurchased: int
    consumablesPurchased: int
    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int


class VisionStats(BaseModel):
    visionScore: int
    wardsPlaced: int
    wardsKilled: int
    visionWardsBoughtInGame: int


class PerkSelection(BaseModel):
    perk: int
    var1: int
    var2: int
    var3: int


class PerkStyle(BaseModel):
    description: str
    selections: List[PerkSelection] = []
    style: int


class Perks(BaseModel):
    statPerks: Dict[str, int]
    styles: List[PerkStyle] = []


class AbilityStats(BaseModel):
    spell1Casts: int
    spell2Casts: int
    spell3Casts: int
    spell4Casts: int

    summoner1Id: int
    summoner2Id: int
    summoner1Casts: int
    summoner2Casts: int

    perks: Perks


class PingStats(BaseModel):
    allInPings: int
    assistMePings: int
    basicPings: int
    commandPings: int
    dangerPings: int
    getBackPings: int
    holdPings: int
    onMyWayPings: int
    pushPings: int
    retreatPings: int
    needVisionPings: int
    enemyMissingPings: int
    enemyVisionPings: int
    visionClearedPings: int


class FarmingStats(BaseModel):
    totalMinionsKilled: int
    neutralMinionsKilled: int
    totalAllyJungleMinionsKilled: int
    totalEnemyJungleMinionsKilled: int


class PlayerData(BaseModel):
    identity: PlayerIdentity
    combat: CombatStats
    objectives: ObjectiveStats
    economy: EconomyStats
    vision: VisionStats
    abilityUsage: AbilityStats
    pings: PingStats
    farming: FarmingStats


class TeamInfo(BaseModel):
    teamId: int
    win: bool


class GameContext(BaseModel):
    matchId: str
    platformId: str
    gameId: int
    queueId: int
    mapId: int
    gameMode: str
    gameType: str
    gameVersion: str
    gameName: str
    gameCreation: int
    gameStartTimestamp: int
    gameEndTimestamp: int
    gameDuration: int
    teams: List[TeamInfo]
    participants: List[str]
    gameEndedInSurrender: bool
    endOfGameResult: str


class MatchData(BaseModel):
    game: GameContext
    players: List[PlayerData]
