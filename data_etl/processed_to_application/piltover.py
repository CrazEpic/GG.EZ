from typing import Any, Dict, List


def info_from_raw_piltover_metrics(raw_metrics: List[Dict[str, Any]]):
    season_1_start = 1736380800000  # Jan 9, 2025, milliseconds
    season_2_start = 1745971200000  # Aug 30, 2025, milliseconds
    season_3_start = 1756252800000  # Aug 27, 2025, milliseconds
    year_stats = {
        "season 1": {},
        "season 2": {},
        "season 3": {},
    }

    # ensure games are sorted
    sorted_raw_metrics = sorted(raw_metrics, key=lambda x: x["gameCreation"])

    season_1_games = []
    season_2_games = []
    season_3_games = []

    for m in sorted_raw_metrics:
        creation_date_milliseconds = m["gameCreation"]
        if creation_date_milliseconds < season_1_start:
            continue
        elif creation_date_milliseconds >= season_1_start and creation_date_milliseconds < season_2_start:
            season_1_games.append(m)
        elif creation_date_milliseconds >= season_2_start and creation_date_milliseconds < season_3_start:
            season_2_games.append(m)
        elif creation_date_milliseconds >= season_3_start:
            season_3_games.append(m)

    for season in year_stats:
        avg_kda_percentage_difference = 0
        avg_gold_earned_percentage_difference = 0
        avg_kill_participation_percentage_difference = 0
        avg_objective_participation_ratio_percentage_difference = 0
        avg_vision_score_percentage_difference = 0
        avg_winrate_percentage_difference = 0

        first_half_avg_kda = 0
        first_half_avg_gold_earned = 0
        first_half_avg_kill_participation = 0
        first_half_avg_objective_participation_ratio = 0
        first_half_avg_vision_score = 0
        first_half_avg_winrate = 0
        second_half_avg_kda = 0
        second_half_avg_gold_earned = 0
        second_half_avg_kill_participation = 0
        second_half_avg_objective_participation_ratio = 0
        second_half_avg_vision_score = 0
        second_half_avg_winrate = 0

        first_half_num_games = 0
        second_half_num_games = 0

        first_half_games = []
        second_half_games = []

        if season == "season 1":
            if len(season_1_games) == 0:
                continue
            elif len(season_1_games) == 1:
                first_half_num_games = 1
                second_half_num_games = 0
                first_half_avg_kda = season_1_games[0]["kda"]
                first_half_avg_gold_earned = season_1_games[0]["gold_earned"]
                first_half_avg_kill_participation = season_1_games[0]["kill_participation"]
                first_half_avg_objective_participation_ratio = season_1_games[0]["objective_participation_ratio"]
                first_half_avg_vision_score = season_1_games[0]["vision_score"]
                first_half_avg_winrate = 1.0 if season_1_games[0]["win"] else 0.0
            else:
                mid_index = len(season_1_games) // 2
                first_half_games = season_1_games[:mid_index]
                second_half_games = season_1_games[mid_index:]
        elif season == "season 2":
            if len(season_2_games) == 0:
                continue
            elif len(season_2_games) == 1:
                first_half_num_games = 1
                second_half_num_games = 0
                first_half_avg_kda = season_2_games[0]["kda"]
                first_half_avg_gold_earned = season_2_games[0]["gold_earned"]
                first_half_avg_kill_participation = season_2_games[0]["kill_participation"]
                first_half_avg_objective_participation_ratio = season_2_games[0]["objective_participation_ratio"]
                first_half_avg_vision_score = season_2_games[0]["vision_score"]
                first_half_avg_winrate = 1.0 if season_2_games[0]["win"] else 0.0
            else:
                mid_index = len(season_2_games) // 2
                first_half_games = season_2_games[:mid_index]
                second_half_games = season_2_games[mid_index:]
        elif season == "season 3":
            if len(season_3_games) == 0:
                continue
            elif len(season_3_games) == 1:
                first_half_num_games = 1
                second_half_num_games = 0
                first_half_avg_kda = season_3_games[0]["kda"]
                first_half_avg_gold_earned = season_3_games[0]["gold_earned"]
                first_half_avg_kill_participation = season_3_games[0]["kill_participation"]
                first_half_avg_objective_participation_ratio = season_3_games[0]["objective_participation_ratio"]
                first_half_avg_vision_score = season_3_games[0]["vision_score"]
                first_half_avg_winrate = 1.0 if season_3_games[0]["win"] else 0.0
            else:
                mid_index = len(season_3_games) // 2
                first_half_games = season_3_games[:mid_index]
                second_half_games = season_3_games[mid_index:]
        if len(first_half_games) + len(second_half_games) > 1:
            for game in first_half_games:
                first_half_avg_kda += game["kda"]
                first_half_avg_gold_earned += game["gold_earned"]
                first_half_avg_kill_participation += game["kill_participation"]
                first_half_avg_objective_participation_ratio += game["objective_participation_ratio"]
                first_half_avg_vision_score += game["vision_score"]
                first_half_avg_winrate += 1.0 if game["win"] else 0.0
            first_half_num_games = len(first_half_games)
            first_half_avg_kda /= max(1, first_half_num_games)
            first_half_avg_gold_earned /= max(1, first_half_num_games)
            first_half_avg_kill_participation /= max(1, first_half_num_games)
            first_half_avg_objective_participation_ratio /= max(1, first_half_num_games)
            first_half_avg_vision_score /= max(1, first_half_num_games)
            first_half_avg_winrate /= max(1, first_half_num_games)

            for game in second_half_games:
                second_half_avg_kda += game["kda"]
                second_half_avg_gold_earned += game["gold_earned"]
                second_half_avg_kill_participation += game["kill_participation"]
                second_half_avg_objective_participation_ratio += game["objective_participation_ratio"]
                second_half_avg_vision_score += game["vision_score"]
                second_half_avg_winrate += 1.0 if game["win"] else 0.0
            second_half_num_games = len(second_half_games)
            second_half_avg_kda /= max(1, second_half_num_games)
            second_half_avg_gold_earned /= max(1, second_half_num_games)
            second_half_avg_kill_participation /= max(1, second_half_num_games)
            second_half_avg_objective_participation_ratio /= max(1, second_half_num_games)
            second_half_avg_vision_score /= max(1, second_half_num_games)
            second_half_avg_winrate /= max(1, second_half_num_games)

            avg_kda_percentage_difference = ((second_half_avg_kda - first_half_avg_kda) / max(1e-5, first_half_avg_kda)) * 100
            avg_gold_earned_percentage_difference = ((second_half_avg_gold_earned - first_half_avg_gold_earned) / max(1e-5, first_half_avg_gold_earned)) * 100
            avg_kill_participation_percentage_difference = ((second_half_avg_kill_participation - first_half_avg_kill_participation) / max(1e-5, first_half_avg_kill_participation)) * 100
            avg_objective_participation_ratio_percentage_difference = (
                (second_half_avg_objective_participation_ratio - first_half_avg_objective_participation_ratio) / max(1e-5, first_half_avg_objective_participation_ratio)
            ) * 100
            avg_vision_score_percentage_difference = ((second_half_avg_vision_score - first_half_avg_vision_score) / max(1e-5, first_half_avg_vision_score)) * 100
            avg_winrate_percentage_difference = ((second_half_avg_winrate - first_half_avg_winrate) / max(1e-5, first_half_avg_winrate)) * 100

        year_stats[season] = {
            "first_half_num_games": first_half_num_games,
            "second_half_num_games": second_half_num_games,
            "avg_kda_percentage_difference": avg_kda_percentage_difference,
            "avg_gold_earned_percentage_difference": avg_gold_earned_percentage_difference,
            "avg_kill_participation_percentage_difference": avg_kill_participation_percentage_difference,
            "avg_objective_participation_ratio_percentage_difference": avg_objective_participation_ratio_percentage_difference,
            "avg_vision_score_percentage_difference": avg_vision_score_percentage_difference,
            "avg_winrate_percentage_difference": avg_winrate_percentage_difference,
            "first_half_avg_kda": first_half_avg_kda,
            "first_half_avg_gold_earned": first_half_avg_gold_earned,
            "first_half_avg_kill_participation": first_half_avg_kill_participation,
            "first_half_avg_objective_participation_ratio": first_half_avg_objective_participation_ratio,
            "first_half_avg_vision_score": first_half_avg_vision_score,
            "first_half_avg_winrate": first_half_avg_winrate,
            "second_half_avg_kda": second_half_avg_kda,
            "second_half_avg_gold_earned": second_half_avg_gold_earned,
            "second_half_avg_kill_participation": second_half_avg_kill_participation,
            "second_half_avg_objective_participation_ratio": second_half_avg_objective_participation_ratio,
            "second_half_avg_vision_score": second_half_avg_vision_score,
            "second_half_avg_winrate": second_half_avg_winrate,
        }
    return year_stats
