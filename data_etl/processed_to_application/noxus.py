from typing import Any, Dict, List


def info_from_raw_noxus_metrics(raw_metrics: List[Dict[str, Any]]):
    total_physical_damage_dealt_to_champions = 0
    total_magic_damage_dealt_to_champions = 0
    total_true_damage_dealt_to_champions = 0

    total_kills = 0
    total_assists = 0
    total_kda = 0
    total_first_bloods = 0

    total_double_kills = 0
    total_triple_kills = 0
    total_quadra_kills = 0
    total_penta_kills = 0

    highest_largest_killing_spree = 0
    total_team_damage_share = 0

    for m in raw_metrics:
        total_physical_damage_dealt_to_champions += m["physical_damage_dealt_to_champions"]
        total_magic_damage_dealt_to_champions += m["magic_damage_dealt_to_champions"]
        total_true_damage_dealt_to_champions += m["true_damage_dealt_to_champions"]
        total_kills += m["kills"]
        total_assists += m["assists"]
        total_kda += m["kda"]
        total_first_bloods += 1 if m["first_blood"] else 0
        total_double_kills += m["double_kills"]
        total_triple_kills += m["triple_kills"]
        total_quadra_kills += m["quadra_kills"]
        total_penta_kills += m["penta_kills"]
        highest_largest_killing_spree = max(highest_largest_killing_spree, m["largest_killing_spree"])
        total_team_damage_share += m["team_damage_share"]
    avg_kda = total_kda / max(1, len(raw_metrics))
    avg_team_damage_share = total_team_damage_share / max(1, len(raw_metrics))
    return {
        "total_physical_damage_dealt_to_champions": total_physical_damage_dealt_to_champions,
        "total_magic_damage_dealt_to_champions": total_magic_damage_dealt_to_champions,
        "total_true_damage_dealt_to_champions": total_true_damage_dealt_to_champions,
        "total_kills": total_kills,
        "total_assists": total_assists,
        "avg_kda": avg_kda,
        "total_first_bloods": total_first_bloods,
        "total_double_kills": total_double_kills,
        "total_triple_kills": total_triple_kills,
        "total_quadra_kills": total_quadra_kills,
        "total_penta_kills": total_penta_kills,
        "highest_largest_killing_spree": highest_largest_killing_spree,
        "avg_team_damage_share": avg_team_damage_share,
    }
