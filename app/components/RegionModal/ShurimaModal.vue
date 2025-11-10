<template>
	<div class="w-full h-full bg-shurima-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="shurimaData" />
		<div class="px-4 sm:px-16">
			<SmallerRegionSharedCardCollector v-bind="shurimaStats" />
			<SmallerRegionSharedAchievements v-bind="shurimaAchievements" />
			<SmallerRegionSharedContinue v-bind="shurimaContinue" @close_modal="$emit('close_modal')" />
		</div>
	</div>
</template>

<script setup lang="ts">
const playerDataStore = usePlayerDataStore()
const totalTurretKills = playerDataStore.playerData?.sr.shurima_info.total_turret_kills
const totalDragonKills = playerDataStore.playerData?.sr.shurima_info.total_dragon_kills
const totalBaronKills = playerDataStore.playerData?.sr.shurima_info.total_baron_kills
const totalHeraldKills = playerDataStore.playerData?.sr.shurima_info.total_herald_kills
const totalAtakhanKills = playerDataStore.playerData?.sr.shurima_info.total_atakhan_kills
const totalFirstTowerKills = playerDataStore.playerData?.sr.shurima_info.total_first_tower_kill
const totalFirstDragonKills = playerDataStore.playerData?.sr.shurima_info.total_first_dragon_kill
const totalFirstBaronKills = playerDataStore.playerData?.sr.shurima_info.total_first_baron_kill
const totalFirstRiftHeraldKills = playerDataStore.playerData?.sr.shurima_info.total_first_rift_herald_kill
const totalObjParticipationRatio = Number(playerDataStore.playerData?.sr.shurima_info.avg_objective_participation_ratio.toFixed(2))
const totalDamageDealtObj = playerDataStore.playerData?.sr.shurima_info.total_damage_dealt_to_objectives
const totalDamageDealtStructures = playerDataStore.playerData?.sr.shurima_info.total_damage_dealt_to_structures

const shurimaData = {
	backdropImage: "/region-backdrop/shurimabackdrop.png",
	title: "The shurima",
	description: "Reclaim Legacy Through Structure and Dominion",
	bgColor: "bg-shurima-secondary",
	borderColor: "border-shurima-primary",
}

const shurimaStats = {
	borderColor: "border-shurima-primary",
	stats: [
		{ title: "Total Turret Kills", value: totalTurretKills },
		{ title: "Total Objectives", value: {totalDragonKills, totalBaronKills, totalHeraldKills, totalAtakhanKills} },
		{ title: "Average Objective Participation", value: totalObjParticipationRatio },
		{ title: "First Objectives Taken", value: {totalFirstTowerKills, totalFirstDragonKills, totalFirstBaronKills, totalFirstRiftHeraldKills} },
		{ title: "Total Damage Dealt to Objectives", value: totalDamageDealtObj },
		{ title: "Total Damage Dealt to Structures", value: totalDamageDealtStructures },
	],
}

const shurimaAchievements = {
	bgColor: "bg-shurima-secondary",
	borderColor: "border-shurima-primary",
	sectionText: "YOUR ACHIEVEMENTS",
	achievementText: "Your longest game was on 11/2/2025, lasting 100 minutes. And yada YADA YADA",
}

const shurimaContinue = {
	bgColor: "bg-shurima-secondary",
	borderColor: "border-shurima-primary",
	continueText: "YOU'VE EARNED YOUR ASCENSION",
	buttonText: "Continue Your Journey",
}
// network fetching
</script>
