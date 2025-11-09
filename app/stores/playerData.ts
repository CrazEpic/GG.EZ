export interface Root {
	sr: Sr
	aram: Aram
}

export interface Sr {
	ionia_info: IoniaInfo
	demacia_info: DemaciaInfo
	targon_info: TargonInfo
	piltover_info: PiltoverInfo
	zaun_info: ZaunInfo
	bilgewater_info: BilgewaterInfo
	shadow_isles_info: ShadowIslesInfo
	shurima_info: ShurimaInfo
	ixtal_info: IxtalInfo
	noxus_info: NoxusInfo
	freljord_info: FreljordInfo
}

export interface Aram {
	demacia_info: DemaciaInfo
	piltover_info: PiltoverInfo
	zaun_info: ZaunInfo
	bilgewater_info: BilgewaterInfo
	shadow_isles_info: ShadowIslesInfo
	noxus_info: NoxusInfo
	freljord_info: FreljordInfo
}

export interface IoniaInfo {
	combat_effectiveness: number
	team_contribution: number
	resource_efficiency: number
	vision_awareness: number
	consistency: number
}

export interface DemaciaInfo {
	most_common_teammates: MostCommonTeammate[]
}

export interface MostCommonTeammate {
	puuid: string
	riotIdGameName: string
	riotIdTagline: string
	matches: number
	wins: number
}

export interface TargonInfo {
	most_played_champion: [string, number]
	q_ability_casts: number
	w_ability_casts: number
	e_ability_casts: number
	r_ability_casts: number
	play_time: number
	game_count: number
	win: number
	kills: number
	deaths: number
	assists: number
	kda: number
	gold_earned: number
	jungle_minions_killed: number
	minions_killed: number
	top_3_items: number[][]
	most_used_keystone_rune: number[]
	top_2_summoner_spells: number[][]
	first_blood: number
	double_kills: number
	triple_kills: number
	quadra_kills: number
	penta_kills: number
	solo_kills: number
	highest_kda: number
	highest_winstreak: number
}

export interface PiltoverInfo {}

export interface ZaunInfo {}

export interface BilgewaterInfo {
	total_gold_earned: number
	avg_cs_per_min: number
	top_3_items: number[][]
	highest_shutdown_bounty: number
	total_shutdown_bounty: number
	most_gold_in_single_game: number
	most_cs_in_single_game: number
}

export interface ShadowIslesInfo {
	total_deaths: number
	total_time_spent_dead: number
	max_deaths_in_a_game: number
	death_ratio: number
	total_revenge_kills: number
	surrender_count: number
	death_positions: number[][]
}

export interface ShurimaInfo {
	total_turret_kills: number
	total_dragon_kills: number
	total_baron_kills: number
	total_herald_kills: number
	total_atakhan_kills: number
	total_first_tower_kill: number
	total_first_dragon_kill: number
	total_first_baron_kill: number
	total_first_rift_herald_kill: number
	avg_objective_participation_ratio: number
	total_damage_dealt_to_objectives: number
	total_damage_dealt_to_structures: number
}

export interface IxtalInfo {
	total_allInPings: number
	total_assistMePings: number
	total_basicPings: number
	total_commandPings: number
	total_dangerPings: number
	total_getBackPings: number
	total_holdPings: number
	total_onMyWayPings: number
	total_pushPings: number
	total_retreatPings: number
	total_needVisionPings: number
	total_enemyMissingPings: number
	total_enemyVisionPings: number
	total_visionClearedPings: number
	total_objectives_stolen: number
	avg_vision_score_per_min: number
	avg_jungle_share_when_jungle: number
	total_total_wards_placed: number
	total_total_wards_killed: number
}

export interface NoxusInfo {
	total_physical_damage_dealt_to_champions: number
	total_magic_damage_dealt_to_champions: number
	total_true_damage_dealt_to_champions: number
	total_kills: number
	total_assists: number
	avg_kda: number
	total_first_bloods: number
	total_double_kills: number
	total_triple_kills: number
	total_quadra_kills: number
	total_penta_kills: number
	highest_largest_killing_spree: number
	avg_team_damage_share: number
}

export interface FreljordInfo {
	total_play_time: number
	total_physical_damage_taken: number
	total_magic_damage_taken: number
	total_true_damage_taken: number
	total_damage_self_mitigated: number
	total_heal: number
	total_heals_on_teammates: number
	avg_survival_ratio: number
	total_snowball_throws: number
}

export const usePlayerDataStore = defineStore("playerData", () => {
	const playerData = ref<Root | null>(null)

	return {
		playerData,
	}
})
