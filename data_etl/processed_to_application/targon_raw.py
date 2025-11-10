from match_model import MatchData
from timeline_model import MatchTimelineData


def get_raw_targon_metrics_for_match(puuid: str, match_data: MatchData, timeline_data: MatchTimelineData):
    player = match_data.players[next(i for i, p in enumerate(match_data.players) if p.identity.puuid == puuid)]
    champion = player.identity.championName
    q_ability_casts = player.abilityUsage.spell1Casts
    w_ability_casts = player.abilityUsage.spell2Casts
    e_ability_casts = player.abilityUsage.spell3Casts
    r_ability_casts = player.abilityUsage.spell4Casts

    play_time = player.combat.timePlayed / 60
    game_count = 1
    win = match_data.game.teams[next(i for i, t in enumerate(match_data.game.teams) if t.teamId == player.identity.teamId)].win

    kills = player.combat.kills
    deaths = player.combat.deaths
    assists = player.combat.assists
    kda = (kills + assists) / max(1, deaths)

    gold_earned = player.economy.goldEarned
    jungle_minions_killed = player.farming.neutralMinionsKilled + player.farming.totalAllyJungleMinionsKilled + player.farming.totalEnemyJungleMinionsKilled
    minions_killed = player.farming.totalMinionsKilled - jungle_minions_killed

    items = [player.economy.item0, player.economy.item1, player.economy.item2, player.economy.item3, player.economy.item4, player.economy.item5, player.economy.item6]
    keystone_rune = player.abilityUsage.perks.styles[0].selections[0].perk if player.abilityUsage.perks.styles else None
    summoner_spells_1 = player.abilityUsage.summoner1Id
    summoner_spells_2 = player.abilityUsage.summoner2Id
    summoner_spells_1_casts = player.abilityUsage.summoner1Casts
    summoner_spells_2_casts = player.abilityUsage.summoner2Casts

    first_blood = player.combat.firstBloodKill
    double_kills = player.combat.doubleKills
    triple_kills = player.combat.tripleKills
    quadra_kills = player.combat.quadraKills
    penta_kills = player.combat.pentaKills
    solo_kills = kills - double_kills - triple_kills - quadra_kills - penta_kills

    return {
        "champion": champion,
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
        "kda": kda,
        "gold_earned": gold_earned,
        "jungle_minions_killed": jungle_minions_killed,
        "minions_killed": minions_killed,
        "items": items,
        "keystone_rune": keystone_rune,
        "summoner_spells_1": summoner_spells_1,
        "summoner_spells_2": summoner_spells_2,
        "summoner_spells_1_casts": summoner_spells_1_casts,
        "summoner_spells_2_casts": summoner_spells_2_casts,
        "first_blood": first_blood,
        "double_kills": double_kills,
        "triple_kills": triple_kills,
        "quadra_kills": quadra_kills,
        "penta_kills": penta_kills,
        "solo_kills": solo_kills,
    }
