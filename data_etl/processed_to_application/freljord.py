from typing import Any, Dict, List


def info_from_raw_freljord_metrics(raw_metrics: List[Dict[str, Any]]):
    total_play_time = 0
    total_physical_damage_taken = 0
    total_magic_damage_taken = 0
    total_true_damage_taken = 0
    total_damage_self_mitigated = 0
    total_heal = 0
    total_heals_on_teammates = 0
    total_survival_ratio = 0
    total_snowball_throws = 0
    for m in raw_metrics:
        total_play_time += m["time_played"]
        total_physical_damage_taken += m["physical_damage_taken"]
        total_magic_damage_taken += m["magic_damage_taken"]
        total_true_damage_taken += m["true_damage_taken"]
        total_damage_self_mitigated += m["damage_self_mitigated"]
        total_heal += m["total_heal"]
        total_heals_on_teammates += m["total_heals_on_teammates"]
        total_survival_ratio += m["survival_ratio"]
        total_snowball_throws += m["snowball_throws"]
    avg_survival_ratio = total_survival_ratio / max(1, len(raw_metrics))
    return {
        "total_play_time": total_play_time,
        "total_physical_damage_taken": total_physical_damage_taken,
        "total_magic_damage_taken": total_magic_damage_taken,
        "total_true_damage_taken": total_true_damage_taken,
        "total_damage_self_mitigated": total_damage_self_mitigated,
        "total_heal": total_heal,
        "total_heals_on_teammates": total_heals_on_teammates,
        "avg_survival_ratio": avg_survival_ratio,
        "total_snowball_throws": total_snowball_throws,
    }
