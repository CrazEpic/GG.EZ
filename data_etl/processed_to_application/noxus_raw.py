from match_model import MatchData
from timeline_model import MatchTimelineData


def get_raw_noxus_metrics_for_match(puuid: str, match_data: MatchData, timeline_data: MatchTimelineData):
    player = match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)]
    physical_damage_dealt_to_champions = player.combat.physicalDamageDealtToChampions
    magic_damage_dealt_to_champions = player.combat.magicDamageDealtToChampions
    true_damage_dealt_to_champions = player.combat.trueDamageDealtToChampions

    kills = player.combat.kills
    assists = player.combat.assists
    deaths = player.combat.deaths
    kda = (kills + assists) / max(1, deaths)
    first_blood = player.combat.firstBloodKill

    double_kills = player.combat.doubleKills
    triple_kills = player.combat.tripleKills
    quadra_kills = player.combat.quadraKills
    penta_kills = player.combat.pentaKills

    largest_killing_spree = player.combat.largestKillingSpree

    total_team_damage_to_champions = 0
    for p in match_data.players:
        if p.identity.teamId == player.identity.teamId:
            total_team_damage_to_champions += p.combat.totalDamageDealtToChampions
    team_damage_share = (physical_damage_dealt_to_champions + magic_damage_dealt_to_champions + true_damage_dealt_to_champions) / max(1, total_team_damage_to_champions)
    return {
        "physical_damage_dealt_to_champions": physical_damage_dealt_to_champions,
        "magic_damage_dealt_to_champions": magic_damage_dealt_to_champions,
        "true_damage_dealt_to_champions": true_damage_dealt_to_champions,
        "kills": kills,
        "assists": assists,
        "kda": kda,
        "first_blood": first_blood,
        "double_kills": double_kills,
        "triple_kills": triple_kills,
        "quadra_kills": quadra_kills,
        "penta_kills": penta_kills,
        "largest_killing_spree": largest_killing_spree,
        "team_damage_share": team_damage_share,
    }
