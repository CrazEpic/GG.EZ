from typing import List, Optional, Dict
from pydantic import BaseModel, Field, ConfigDict, RootModel


class SummonerDTO(BaseModel):
    profileIconId: int
    puuid: str
    summonerLevel: int
    revisionDate: int
    model_config = ConfigDict(extra="ignore")


class MiniSeriesDTO(BaseModel):
    losses: int
    progress: str
    target: int
    wins: int
    model_config = ConfigDict(extra="ignore")


class LeagueEntryDTO(BaseModel):
    leagueId: str
    puuid: str
    queueType: str
    tier: str
    rank: str
    leaguePoints: int
    wins: int
    losses: int
    hotStreak: bool
    veteran: bool
    freshBlood: bool
    inactive: bool
    miniSeries: Optional[MiniSeriesDTO] = None
    model_config = ConfigDict(extra="ignore")


class MissionsDTO(BaseModel):
    playerScore0: int
    playerScore1: int
    playerScore2: int
    playerScore3: int
    playerScore4: int
    playerScore5: int
    playerScore6: int
    playerScore7: int
    playerScore8: int
    playerScore9: int
    playerScore10: int
    playerScore11: int
    model_config = ConfigDict(extra="ignore")


# class ChallengesDTO(BaseModel):
#     assistStreakCount: int = Field(alias="12AssistStreakCount")
#     baronBuffGoldAdvantageOverThreshold: int
#     controlWardTimeCoverageInRiverOrEnemyHalf: float
#     earliestBaron: int
#     earliestDragonTakedown: int
#     earliestElderDragon: int
#     earlyLaningPhaseGoldExpAdvantage: int
#     fasterSupportQuestCompletion: int
#     fastestLegendary: int
#     hadAfkTeammate: int
#     highestChampionDamage: int
#     highestCrowdControlScore: int
#     highestWardKills: int
#     junglerKillsEarlyJungle: int
#     killsOnLanersEarlyJungleAsJungler: int
#     laningPhaseGoldExpAdvantage: int
#     legendaryCount: int
#     maxCsAdvantageOnLaneOpponent: float
#     maxLevelLeadLaneOpponent: int
#     mostWardsDestroyedOneSweeper: int
#     mythicItemUsed: int
#     playedChampSelectPosition: int
#     soloTurretsLategame: int
#     takedownsFirst25Minutes: int
#     teleportTakedowns: int
#     thirdInhibitorDestroyedTime: int
#     threeWardsOneSweeperCount: int
#     visionScoreAdvantageLaneOpponent: float
#     InfernalScalePickup: int
#     fistBumpParticipation: int
#     voidMonsterKill: int
#     abilityUses: int
#     acesBefore15Minutes: int
#     alliedJungleMonsterKills: float
#     baronTakedowns: int
#     blastConeOppositeOpponentCount: int
#     bountyGold: int
#     buffsStolen: int
#     completeSupportQuestInTime: int
#     controlWardsPlaced: int
#     damagePerMinute: float
#     damageTakenOnTeamPercentage: float
#     dancedWithRiftHerald: int
#     deathsByEnemyChamps: int
#     dodgeSkillShotsSmallWindow: int
#     doubleAces: int
#     dragonTakedowns: int
#     legendaryItemUsed: List[int]
#     effectiveHealAndShielding: float
#     elderDragonKillsWithOpposingSoul: int
#     elderDragonMultikills: int
#     enemyChampionImmobilizations: int
#     enemyJungleMonsterKills: float
#     epicMonsterKillsNearEnemyJungler: int
#     epicMonsterKillsWithin30SecondsOfSpawn: int
#     epicMonsterSteals: int
#     epicMonsterStolenWithoutSmite: int
#     firstTurretKilled: int
#     firstTurretKilledTime: float
#     flawlessAces: int
#     fullTeamTakedown: int
#     gameLength: float
#     getTakedownsInAllLanesEarlyJungleAsLaner: int
#     goldPerMinute: float
#     hadOpenNexus: int
#     immobilizeAndKillWithAlly: int
#     initialBuffCount: int
#     initialCrabCount: int
#     jungleCsBefore10Minutes: float
#     junglerTakedownsNearDamagedEpicMonster: int
#     kda: float
#     killAfterHiddenWithAlly: int
#     killedChampTookFullTeamDamageSurvived: int
#     killingSprees: int
#     killParticipation: float
#     killsNearEnemyTurret: int
#     killsOnOtherLanesEarlyJungleAsLaner: int
#     killsOnRecentlyHealedByAramPack: int
#     killsUnderOwnTurret: int
#     killsWithHelpFromEpicMonster: int
#     knockEnemyIntoTeamAndKill: int
#     kTurretsDestroyedBeforePlatesFall: int
#     landSkillShotsEarlyGame: int
#     laneMinionsFirst10Minutes: int
#     lostAnInhibitor: int
#     maxKillDeficit: int
#     mejaisFullStackInTime: int
#     moreEnemyJungleThanOpponent: float
#     multiKillOneSpell: int
#     multikills: int
#     multikillsAfterAggressiveFlash: int
#     multiTurretRiftHeraldCount: int
#     outerTurretExecutesBefore10Minutes: int
#     outnumberedKills: int
#     outnumberedNexusKill: int
#     perfectDragonSoulsTaken: int
#     perfectGame: int
#     pickKillWithAlly: int
#     poroExplosions: int
#     quickCleanse: int
#     quickFirstTurret: int
#     quickSoloKills: int
#     riftHeraldTakedowns: int
#     saveAllyFromDeath: int
#     scuttleCrabKills: int
#     shortestTimeToAceFromFirstTakedown: float
#     skillshotsDodged: int
#     skillshotsHit: int
#     snowballsHit: int
#     soloBaronKills: int
#     SWARM_DefeatAatrox: int
#     SWARM_DefeatBriar: int
#     SWARM_DefeatMiniBosses: int
#     SWARM_EvolveWeapon: int
#     SWARM_Have3Passives: int
#     SWARM_KillEnemy: int
#     SWARM_PickupGold: float
#     SWARM_ReachLevel50: int
#     SWARM_Survive15Min: int
#     SWARM_WinWith5EvolvedWeapons: int
#     soloKills: int
#     stealthWardsPlaced: int
#     survivedSingleDigitHpCount: int
#     survivedThreeImmobilizesInFight: int
#     takedownOnFirstTurret: int
#     takedowns: int
#     takedownsAfterGainingLevelAdvantage: int
#     takedownsBeforeJungleMinionSpawn: int
#     takedownsFirstXMinutes: int
#     takedownsInAlcove: int
#     takedownsInEnemyFountain: int
#     teamBaronKills: int
#     teamDamagePercentage: float
#     teamElderDragonKills: int
#     teamRiftHeraldKills: int
#     tookLargeDamageSurvived: int
#     turretPlatesTaken: int
#     turretsTakenWithRiftHerald: int
#     turretTakedowns: int
#     twentyMinionsIn3SecondsCount: int
#     twoWardsOneSweeperCount: int
#     unseenRecalls: int
#     visionScorePerMinute: float
#     wardsGuarded: int
#     wardTakedowns: int
#     wardTakedownsBefore20M: int
#     model_config = ConfigDict(extra="ignore")


class ChallengesDTO(BaseModel):
    model_config = ConfigDict(extra="ignore")


class PerkStatsDTO(BaseModel):
    defense: int
    flex: int
    offense: int
    model_config = ConfigDict(extra="ignore")


class PerkStyleSelectionDTO(BaseModel):
    perk: int
    var1: int
    var2: int
    var3: int
    model_config = ConfigDict(extra="ignore")


class PerkStyleDTO(BaseModel):
    description: str
    selections: List[PerkStyleSelectionDTO]
    style: int
    model_config = ConfigDict(extra="ignore")


class PerksDTO(BaseModel):
    statPerks: PerkStatsDTO
    styles: List[PerkStyleDTO]
    model_config = ConfigDict(extra="ignore")


class ParticipantDTO(BaseModel):
    allInPings: int
    assistMePings: int
    assists: int
    baronKills: int
    # bountyLevel: int
    bountyLevel: Optional[int] = None
    champExperience: int
    champLevel: int
    championId: int
    championName: str
    commandPings: int
    championTransform: int
    consumablesPurchased: int
    challenges: ChallengesDTO
    damageDealtToBuildings: int
    damageDealtToObjectives: int
    damageDealtToTurrets: int
    damageSelfMitigated: int
    deaths: int
    detectorWardsPlaced: int
    doubleKills: int
    dragonKills: int
    eligibleForProgression: bool
    enemyMissingPings: int
    enemyVisionPings: int
    firstBloodAssist: bool
    firstBloodKill: bool
    firstTowerAssist: bool
    firstTowerKill: bool
    gameEndedInEarlySurrender: bool
    gameEndedInSurrender: bool
    holdPings: int
    getBackPings: int
    goldEarned: int
    goldSpent: int
    individualPosition: str
    inhibitorKills: int
    inhibitorTakedowns: int
    inhibitorsLost: int
    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int
    itemsPurchased: int
    killingSprees: int
    kills: int
    lane: str
    largestCriticalStrike: int
    largestKillingSpree: int
    largestMultiKill: int
    longestTimeSpentLiving: int
    magicDamageDealt: int
    magicDamageDealtToChampions: int
    magicDamageTaken: int
    missions: MissionsDTO
    neutralMinionsKilled: int
    needVisionPings: int
    nexusKills: int
    nexusTakedowns: int
    nexusLost: int
    objectivesStolen: int
    objectivesStolenAssists: int
    onMyWayPings: int
    participantId: int
    playerScore0: int = Field(alias="PlayerScore0")
    playerScore1: int = Field(alias="PlayerScore1")
    playerScore2: int = Field(alias="PlayerScore2")
    playerScore3: int = Field(alias="PlayerScore3")
    playerScore4: int = Field(alias="PlayerScore4")
    playerScore5: int = Field(alias="PlayerScore5")
    playerScore6: int = Field(alias="PlayerScore6")
    playerScore7: int = Field(alias="PlayerScore7")
    playerScore8: int = Field(alias="PlayerScore8")
    playerScore9: int = Field(alias="PlayerScore9")
    playerScore10: int = Field(alias="PlayerScore10")
    playerScore11: int = Field(alias="PlayerScore11")
    pentaKills: int
    perks: Optional[PerksDTO] = None
    physicalDamageDealt: int
    physicalDamageDealtToChampions: int
    physicalDamageTaken: int
    placement: int
    playerAugment1: int
    playerAugment2: int
    playerAugment3: int
    playerAugment4: int
    playerSubteamId: int
    pushPings: int
    puuid: str
    profileIcon: int
    quadraKills: int
    riotIdGameName: str
    riotIdTagline: str
    role: str
    sightWardsBoughtInGame: int
    spell1Casts: int
    spell2Casts: int
    spell3Casts: int
    spell4Casts: int
    subteamPlacement: int
    summoner1Casts: int
    summoner1Id: int
    summoner2Casts: int
    summoner2Id: int
    summonerId: str
    summonerLevel: int
    summonerName: str
    teamEarlySurrendered: bool
    teamId: int
    teamPosition: str
    timeCCingOthers: int
    timePlayed: int
    totalAllyJungleMinionsKilled: int
    totalDamageDealt: int
    totalDamageDealtToChampions: int
    totalDamageShieldedOnTeammates: int
    totalDamageTaken: int
    totalEnemyJungleMinionsKilled: int
    totalHeal: int
    totalHealsOnTeammates: int
    totalMinionsKilled: int
    totalTimeCCDealt: int
    totalTimeSpentDead: int
    totalUnitsHealed: int
    tripleKills: int
    trueDamageDealt: int
    trueDamageDealtToChampions: int
    trueDamageTaken: int
    turretKills: int
    turretTakedowns: int
    turretsLost: int
    unrealKills: int
    visionScore: int
    visionClearedPings: int
    visionWardsBoughtInGame: int
    wardsKilled: int
    wardsPlaced: int
    win: bool
    model_config = ConfigDict(extra="ignore")


class MetadataDTO(BaseModel):
    dataVersion: str
    matchId: str
    participants: List[str]
    model_config = ConfigDict(extra="ignore")


class BanDTO(BaseModel):
    championId: int
    pickTurn: int
    model_config = ConfigDict(extra="ignore")


class ObjectiveDTO(BaseModel):
    first: bool
    kills: int
    model_config = ConfigDict(extra="ignore")


class ObjectivesDTO(BaseModel):
    baron: ObjectiveDTO
    champion: ObjectiveDTO
    dragon: ObjectiveDTO
    horde: ObjectiveDTO
    inhibitor: ObjectiveDTO
    riftHerald: ObjectiveDTO
    tower: ObjectiveDTO
    model_config = ConfigDict(extra="ignore")


class TeamDTO(BaseModel):
    bans: List[BanDTO]
    objectives: ObjectivesDTO
    teamId: int
    win: bool
    model_config = ConfigDict(extra="ignore")


class InfoDTO(BaseModel):
    endOfGameResult: str
    gameCreation: int
    gameDuration: int
    gameEndTimestamp: int
    gameId: int
    gameMode: str
    gameName: str
    gameStartTimestamp: int
    gameType: str
    gameVersion: str
    mapId: int
    participants: List[ParticipantDTO]
    platformId: str
    queueId: int
    teams: List[TeamDTO]
    tournamentCode: Optional[str] = None
    model_config = ConfigDict(extra="ignore")


class MatchDTO(BaseModel):
    metadata: MetadataDTO
    info: InfoDTO
    model_config = ConfigDict(extra="ignore")


class AccountDTO(BaseModel):
    puuid: str
    gameName: str
    tagLine: str
    model_config = ConfigDict(extra="ignore")


class PositionDto(BaseModel):
    x: int = None
    y: int = None
    model_config = ConfigDict(extra="ignore")


class DamageStatsDto(BaseModel):
    magicDamageDone: int = None
    magicDamageDoneToChampions: int = None
    magicDamageTaken: int = None
    physicalDamageDone: int = None
    physicalDamageDoneToChampions: int = None
    physicalDamageTaken: int = None
    totalDamageDone: int = None
    totalDamageDoneToChampions: int = None
    totalDamageTaken: int = None
    trueDamageDone: int = None
    trueDamageDoneToChampions: int = None
    trueDamageTaken: int = None
    model_config = ConfigDict(extra="ignore")


class ChampionStatsDto(BaseModel):
    abilityHaste: int = None
    abilityPower: int = None
    armor: int = None
    armorPen: int = None
    armorPenPercent: int = None
    attackDamage: int = None
    attackSpeed: int = None
    bonusArmorPenPercent: int = None
    bonusMagicPenPercent: int = None
    ccReduction: int = None
    cooldownReduction: int = None
    health: int = None
    healthMax: int = None
    healthRegen: int = None
    lifesteal: int = None
    magicPen: int = None
    magicPenPercent: int = None
    magicResist: int = None
    movementSpeed: int = None
    omnivamp: int = None
    physicalVamp: int = None
    power: int = None
    powerMax: int = None
    powerRegen: int = None
    spellVamp: int = None
    model_config = ConfigDict(extra="ignore")


class ParticipantFrameDto(BaseModel):
    championStats: ChampionStatsDto = None
    currentGold: int = None
    damageStats: DamageStatsDto = None
    goldPerSecond: int = None
    jungleMinionsKilled: int = None
    level: int = None
    minionsKilled: int = None
    participantId: int = None
    position: PositionDto = None
    timeEnemySpentControlled: int = None
    totalGold: int = None
    xp: int = None
    model_config = ConfigDict(extra="ignore")


class ParticipantFramesDto(RootModel):
    root: Dict[str, ParticipantFrameDto] = None


class EventsTimeLineDto(BaseModel):
    timestamp: int = None
    realTimestamp: int = None
    type: str = None
    model_config = ConfigDict(extra="ignore")


class FramesTimeLineDto(BaseModel):
    events: List[EventsTimeLineDto] = None
    participantFrames: ParticipantFramesDto = None
    timestamp: int = None
    model_config = ConfigDict(extra="ignore")


class ParticipantTimeLineDto(BaseModel):
    participantId: int = None
    puuid: str = None
    model_config = ConfigDict(extra="ignore")


class InfoTimeLineDto(BaseModel):
    endOfGameResult: str = None
    frameInterval: int = None
    gameId: int = None
    participants: List[ParticipantTimeLineDto] = None
    frames: List[FramesTimeLineDto] = None
    model_config = ConfigDict(extra="ignore")


class MetadataTimeLineDto(BaseModel):
    dataVersion: str = None
    matchId: str = None
    participants: List[str] = None
    model_config = ConfigDict(extra="ignore")


class TimelineDto(BaseModel):
    metadata: MetadataTimeLineDto = None
    info: InfoTimeLineDto = None
    model_config = ConfigDict(extra="ignore")
