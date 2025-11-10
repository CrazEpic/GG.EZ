from typing import Any, Dict, List


def info_from_raw_zaun_metrics(raw_metrics: List[Dict[str, Any]]):
    season_1_start = 1736380800000  # Jan 9, 2025, milliseconds
    season_2_start = 1745971200000  # Aug 30, 2025, milliseconds
    season_3_start = 1756252800000  # Aug 27, 2025, milliseconds
    year_stats = {
        "season 1": {},
        "season 2": {},
        "season 3": {},
    }
    for season in year_stats:
        max_pentakills = 0
        max_gold_deficit_comeback = 0
        max_kills = 0
        max_deaths = 0
        current_win_streak = 0
        current_loss_streak = 0
        biggest_win_streak = 0
        biggest_loss_streak = 0
        max_damage_dealt = 0
        max_damage_taken = 0
        num_games = 0

        for m in raw_metrics:
            creation_date_milliseconds = m["gameCreation"]
            if creation_date_milliseconds < season_1_start:
                continue
            elif season == "season 1" and creation_date_milliseconds >= season_1_start and creation_date_milliseconds < season_2_start:
                pass
            elif season == "season 2" and creation_date_milliseconds >= season_2_start and creation_date_milliseconds < season_3_start:
                pass
            elif season == "season 3" and creation_date_milliseconds >= season_3_start:
                pass
            else:
                continue
            num_games += 1

            max_pentakills = max(max_pentakills, m["pentakills"])
            if m["win"]:
                max_gold_deficit_comeback = max(max_gold_deficit_comeback, m["max_gold_deficit"])
            max_kills = max(max_kills, m["kills"])
            max_deaths = max(max_deaths, m["deaths"])
            max_damage_dealt = max(max_damage_dealt, m["damage_dealt"])
            max_damage_taken = max(max_damage_taken, m["damage_taken"])
            if m["win"]:
                current_win_streak += 1
                biggest_win_streak = max(biggest_win_streak, current_win_streak)
                current_loss_streak = 0
            else:
                current_loss_streak += 1
                biggest_loss_streak = max(biggest_loss_streak, current_loss_streak)
                current_win_streak = 0
        year_stats[season] = {
            "games_played": num_games,
            "max_pentakills": max_pentakills,
            "max_gold_deficit_comeback": max_gold_deficit_comeback,
            "max_kills": max_kills,
            "max_deaths": max_deaths,
            "max_damage_dealt": max_damage_dealt,
            "max_damage_taken": max_damage_taken,
            "biggest_win_streak": biggest_win_streak,
            "biggest_loss_streak": biggest_loss_streak,
        }
    return year_stats
