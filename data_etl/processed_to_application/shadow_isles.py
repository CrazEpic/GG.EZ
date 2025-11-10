from typing import Any, Dict, List


def info_from_raw_shadow_isles_metrics(raw_metrics: List[Dict[str, Any]]):
    total_play_time = 0
    total_deaths = 0
    total_time_spent_dead = 0
    total_revenge_kills = 0
    surrender_count = 0
    death_position_counter = set()
    max_deaths_in_a_game = 0

    for m in raw_metrics:
        total_play_time += m["play_time"]
        total_deaths += m["deaths"]
        total_time_spent_dead += m["time_spent_dead"]
        total_revenge_kills += m["revenge_kills"]
        if m["game_ended_in_surrender"]:
            surrender_count += 1
        for pos in m["death_positions"]:
            death_position_counter.add(pos)

        max_deaths_in_a_game = max(max_deaths_in_a_game, m["deaths"])

    death_ratio = total_time_spent_dead / max(1, total_play_time)

    return {
        "total_deaths": total_deaths,
        "total_time_spent_dead": total_time_spent_dead,
        "max_deaths_in_a_game": max_deaths_in_a_game,
        "death_ratio": death_ratio,
        "total_revenge_kills": total_revenge_kills,
        "surrender_count": surrender_count,
        "death_positions": list(death_position_counter),
    }
