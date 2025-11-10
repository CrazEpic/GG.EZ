from typing import Any, Dict, List


def info_from_raw_shurima_metrics(raw_metrics: List[Dict[str, Any]]):
    total_turret_kills = 0
    total_dragon_kills = 0
    total_baron_kills = 0
    total_herald_kills = 0
    total_atakhan_kills = 0
    total_first_tower_kill = 0
    total_first_dragon_kill = 0
    total_first_baron_kill = 0
    total_first_rift_herald_kill = 0
    total_objective_participation_ratio = 0
    total_damage_dealt_to_objectives = 0
    total_damage_dealt_to_structures = 0

    for m in raw_metrics:
        total_turret_kills += m["turret_kills"]
        total_dragon_kills += m["dragon_kills"]
        total_baron_kills += m["baron_kills"]
        total_herald_kills += m["herald_kills"]
        total_atakhan_kills += m["atakhan_kills"]
        total_first_tower_kill += 1 if m["first_tower_kill"] else 0
        total_first_dragon_kill += 1 if m["first_dragon_kill"] else 0
        total_first_baron_kill += 1 if m["first_baron_kill"] else 0
        total_first_rift_herald_kill += 1 if m["first_rift_herald_kill"] else 0
        total_objective_participation_ratio += m["objective_participation_ratio"]
        total_damage_dealt_to_objectives += m["damage_dealt_to_objectives"]
        total_damage_dealt_to_structures += m["damage_dealt_to_structures"]

    avg_objective_participation_ratio = total_objective_participation_ratio / max(1, len(raw_metrics))

    return {
        "total_turret_kills": total_turret_kills,
        "total_dragon_kills": total_dragon_kills,
        "total_baron_kills": total_baron_kills,
        "total_herald_kills": total_herald_kills,
        "total_atakhan_kills": total_atakhan_kills,
        "total_first_tower_kill": total_first_tower_kill,
        "total_first_dragon_kill": total_first_dragon_kill,
        "total_first_baron_kill": total_first_baron_kill,
        "total_first_rift_herald_kill": total_first_rift_herald_kill,
        "avg_objective_participation_ratio": avg_objective_participation_ratio,
        "total_damage_dealt_to_objectives": total_damage_dealt_to_objectives,
        "total_damage_dealt_to_structures": total_damage_dealt_to_structures,
    }
