<template>
	<div class="w-full h-full bg-shadowIsles-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="shadowIslesData" />
		<div class="px-4 sm:px-16">
			<SmallerRegionSharedCardCollector v-bind="shadowIslesStats" />
			<SmallerRegionSharedAchievements v-bind="shadowIslesAchievements" />
			<SmallerRegionSharedContinue v-bind="shadowIslesContinue" @close_modal="$emit('close_modal')" />
		</div>
	</div>
</template>

<script setup lang="ts">
const playerDataStore = usePlayerDataStore()
const totalDeaths = playerDataStore.playerData?.sr.shadow_isles_info.total_deaths
const totalTimeSpentDead = Number(playerDataStore.playerData?.sr.shadow_isles_info.total_time_spent_dead.toFixed(0))

const hours = Math.floor(totalTimeSpentDead / 60);
const minutes = totalTimeSpentDead % 60;
const formattedTime = `${hours}h ${Number(minutes.toFixed(0))}m`;

const maxDeathSingleGame = playerDataStore.playerData?.sr.shadow_isles_info.max_deaths_in_a_game
const deathRatio = Number(playerDataStore.playerData?.sr.shadow_isles_info.death_ratio.toFixed(2))
const totalRevengeKills = playerDataStore.playerData?.sr.shadow_isles_info.total_revenge_kills
const gameEndedInSurrender = playerDataStore.playerData?.sr.shadow_isles_info.surrender_count

const shadowIslesData = {
	backdropImage: "/region-backdrop/shadowIslesbackdrop.png",
	title: "The shadowIsles",
	description: "Tenacity Forged in the Black Mist",
	bgColor: "bg-shadowIsles-secondary",
	borderColor: "border-shadowIsles-primary",
}

const shadowIslesStats = {
	borderColor: "border-shadowIsles-primary",
	stats: [
		{ title: "Total Deaths", value: totalDeaths },
		{ title: "Total Time Spent Dead", value: formattedTime },
		{ title: "Death Ratio", value: deathRatio },
		{ title: "Death Heatmap", value: "?" },
		{ title: "Games Forfeited", value: gameEndedInSurrender },
		{ title: "Highest Deaths in a Single Game", value: maxDeathSingleGame },
		{ title: "Total Revenge Kills", value: totalRevengeKills },
	],
}

const shadowIslesAchievements = {
	bgColor: "bg-shadowIsles-secondary",
	borderColor: "border-shadowIsles-primary",
	sectionText: "YOUR ACHIEVEMENTS",
	achievementText: "Your longest game was on 11/2/2025, lasting 100 minutes. And yada YADA YADA",
}

const shadowIslesContinue = {
	bgColor: "bg-shadowIsles-secondary",
	borderColor: "border-shadowIsles-primary",
	continueText: "YOU'VE SURVIVED THE HARROWING",
	buttonText: "Continue Your Journey",
}
// network fetching
</script>
