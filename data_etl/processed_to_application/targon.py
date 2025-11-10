from typing import Any, Dict, List


def info_from_raw_targon_metrics(raw_metrics: List[Dict[str, Any]]):
    champion_counts = {}
    for metric in raw_metrics:
        champion = metric["champion"]
        if champion not in champion_counts:
            champion_counts[champion] = 0
        champion_counts[champion] += 1
    if champion_counts:
        most_played_champion = sorted(champion_counts.items(), key=lambda x: x[1], reverse=True)[0]
        relevant_champion_metrics = [m for m in raw_metrics if m["champion"] == most_played_champion[0]]
    else:
        most_played_champion = (None, 0)
        relevant_champion_metrics = []

    q_ability_casts = 0
    w_ability_casts = 0
    e_ability_casts = 0
    r_ability_casts = 0

    play_time = 0
    game_count = 0
    win = 0

    kills = 0
    deaths = 0
    assists = 0

    gold_earned = 0
    jungle_minions_killed = 0
    minions_killed = 0

    item_counter = {}
    keystone_rune_counter = {}
    summoner_spells_cast_counter = {}

    first_blood = 0
    double_kills = 0
    triple_kills = 0
    quadra_kills = 0
    penta_kills = 0
    solo_kills = 0

    highest_kda = 0
    highest_winstreak = 0
    current_winstreak = 0

    for m in relevant_champion_metrics:
        q_ability_casts += m["q_ability_casts"]
        w_ability_casts += m["w_ability_casts"]
        e_ability_casts += m["e_ability_casts"]
        r_ability_casts += m["r_ability_casts"]
        play_time += m["play_time"]
        game_count += m["game_count"]
        win += m["win"]
        kills += m["kills"]
        deaths += m["deaths"]
        assists += m["assists"]
        gold_earned += m["gold_earned"]
        jungle_minions_killed += m["jungle_minions_killed"]
        minions_killed += m["minions_killed"]
        first_blood += 1 if m["first_blood"] else 0
        double_kills += m["double_kills"]
        triple_kills += m["triple_kills"]
        quadra_kills += m["quadra_kills"]
        penta_kills += m["penta_kills"]
        solo_kills += m["solo_kills"]
        for item in m["items"]:
            if item not in item_counter:
                item_counter[item] = 0
            item_counter[item] += 1
        keystone_rune = m["keystone_rune"]
        if keystone_rune not in keystone_rune_counter:
            keystone_rune_counter[keystone_rune] = 0
        keystone_rune_counter[keystone_rune] += 1
        summoner_spells_1 = m["summoner_spells_1"]
        summoner_spells_2 = m["summoner_spells_2"]
        if summoner_spells_1 not in summoner_spells_cast_counter:
            summoner_spells_cast_counter[summoner_spells_1] = 0
        summoner_spells_cast_counter[summoner_spells_1] += m["summoner_spells_1_casts"]
        if summoner_spells_2 not in summoner_spells_cast_counter:
            summoner_spells_cast_counter[summoner_spells_2] = 0
        summoner_spells_cast_counter[summoner_spells_2] += m["summoner_spells_2_casts"]

        highest_kda = max(highest_kda, m["kda"])
        if m["win"]:
            current_winstreak += 1
            highest_winstreak = max(highest_winstreak, current_winstreak)
        else:
            current_winstreak = 0

    # no item?
    if 0 in item_counter:
        del item_counter[0]
    # don't count trinkets and boots and feats of strength

    # Remove trinkets, boots, and feats of strength from item_counter
    trinket_ids = {3340, 2056, 3364, 3363, 2055}
    boot_ids = {1001, 3006, 3009, 3158, 3111, 3047, 3020, 3010}
    feat_of_strength_ids = {3170, 3171, 3172, 3173, 3174, 3175, 3176}

    for item_id in list(item_counter.keys()):
        if item_id in trinket_ids or item_id in boot_ids or item_id in feat_of_strength_ids:
            del item_counter[item_id]

    # Wards
    # Stealth Ward (Yellow Trinket): 3340
    # The purchasable variant (in the shop) has an ID of 2056

    # Oracle Lens (Red Trinket / Sweeper): 3364

    # Farsight Alteration (Blue Trinket): 3363

    # Control ward: 2055

    # Tier 1 boots
    # Boots: 1001

    # Tier 2 boots
    # Berserker's Greaves: 3006
    # Boots of Swiftness: 3009
    # Ionian Boots of Lucidity: 3158
    # Mercury's Treads: 3111
    # Plated Steelcaps (formerly Ninja Tabi): 3047
    # Sorcerer's Shoes: 3020
    # Symbiote Soles: 3010

    # Feats of strength
    # 3170 swift
    # 3171 lucidity
    # 3172 greaves
    # 3173 treads
    # 3174 steelcaps
    # 3175 sorc
    # 3176 symbiote

    # no keystone rune?
    if None in keystone_rune_counter:
        del keystone_rune_counter[None]

    top_3_items = sorted(item_counter.items(), key=lambda x: x[1], reverse=True)[:3] if item_counter else []
    most_used_keystone_rune = sorted(keystone_rune_counter.items(), key=lambda x: x[1], reverse=True)[0] if keystone_rune_counter else (None, 0)
    top_2_summoner_spells = sorted(summoner_spells_cast_counter.items(), key=lambda x: x[1], reverse=True)[:2] if summoner_spells_cast_counter else []

    return {
        "most_played_champion": most_played_champion,
        "q_ability_casts": q_ability_casts,
        "w_ability_casts": w_ability_casts,
        "e_ability_casts": e_ability_casts,
        "r_ability_casts": r_ability_casts,
        "play_time": play_time,
        "game_count": game_count,
        "win": win,
        "kills": kills,
        "deaths": deaths,
        "assists": assists,
        "kda": (kills + assists) / max(1, deaths),
        "gold_earned": gold_earned,
        "jungle_minions_killed": jungle_minions_killed,
        "minions_killed": minions_killed,
        "top_3_items": top_3_items,
        "most_used_keystone_rune": most_used_keystone_rune,
        "top_2_summoner_spells": top_2_summoner_spells,
        "first_blood": first_blood,
        "double_kills": double_kills,
        "triple_kills": triple_kills,
        "quadra_kills": quadra_kills,
        "penta_kills": penta_kills,
        "solo_kills": solo_kills,
        "highest_kda": highest_kda,
        "highest_winstreak": highest_winstreak,
    }
