from typing import Any, Dict, List


def info_from_raw_bilgewater_metrics(raw_metrics: List[Dict[str, Any]]):
    play_time = 0
    total_gold_earned = 0
    total_jungle_minions_killed = 0
    total_minions_killed = 0
    item_counter = {}
    highest_shutdown_bounty = 0
    total_shutdown_bounty = 0

    most_gold_in_single_game = 0
    most_cs_in_single_game = 0

    for m in raw_metrics:
        play_time += m["play_time"]
        total_gold_earned += m["gold_earned"]
        total_jungle_minions_killed += m["jungle_minions_killed"]
        total_minions_killed += m["minions_killed"]
        highest_shutdown_bounty = max(highest_shutdown_bounty, m["highest_shutdown_bounty"])
        total_shutdown_bounty += m["total_shutdown_bounty"]
        for item in m["items"]:
            if item not in item_counter:
                item_counter[item] = 0
            item_counter[item] += 1
        most_gold_in_single_game = max(most_gold_in_single_game, m["gold_earned"])
        most_cs_in_single_game = max(most_cs_in_single_game, m["jungle_minions_killed"] + m["minions_killed"])

    # no item?
    if 0 in item_counter:
        del item_counter[0]

    top_3_items = sorted(item_counter.items(), key=lambda x: x[1], reverse=True)[:3]

    avg_cs_per_min = (total_jungle_minions_killed + total_minions_killed) / max(1, play_time)

    return {
        "total_gold_earned": total_gold_earned,
        "avg_cs_per_min": avg_cs_per_min,
        "top_3_items": top_3_items,
        "highest_shutdown_bounty": highest_shutdown_bounty,
        "total_shutdown_bounty": total_shutdown_bounty,
        "most_gold_in_single_game": most_gold_in_single_game,
        "most_cs_in_single_game": most_cs_in_single_game,
    }
