from match_model import MatchData
from timeline_model import MatchTimelineData


def get_raw_freljord_metrics_for_match(puuid: str, match_data: MatchData, timeline_data: MatchTimelineData):
    player = match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)]
    time_played = player.combat.timePlayed / 60
    physical_damage_taken = player.combat.physicalDamageTaken
    magic_damage_taken = player.combat.magicDamageTaken
    true_damage_taken = player.combat.trueDamageTaken
    damage_self_mitigated = player.combat.damageSelfMitigated
    total_heal = player.combat.totalHeal
    total_heals_on_teammates = player.combat.totalHealsOnTeammates
    survival_ratio = (player.combat.timePlayed - player.combat.totalTimeSpentDead) / max(1, player.combat.timePlayed)
    snowball_throws = 0
    if player.abilityUsage.summoner1Id == 32:
        snowball_throws = player.abilityUsage.summoner1Casts
    elif player.abilityUsage.summoner2Id == 32:
        snowball_throws = player.abilityUsage.summoner2Casts
    return {
        "time_played": time_played,
        "physical_damage_taken": physical_damage_taken,
        "magic_damage_taken": magic_damage_taken,
        "true_damage_taken": true_damage_taken,
        "damage_self_mitigated": damage_self_mitigated,
        "total_heal": total_heal,
        "total_heals_on_teammates": total_heals_on_teammates,
        "survival_ratio": survival_ratio,
        "snowball_throws": snowball_throws,
    }
