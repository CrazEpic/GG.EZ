<template>
	<div class="w-full h-full bg-noxus-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="noxusData" />
		<div class="px-4 sm:px-16">
			<SmallerRegionSharedCardCollector v-bind="noxusStats" />
			<SmallerRegionSharedAchievements v-bind="noxusAchievements" />
			<SmallerRegionSharedContinue v-bind="noxusContinue" @close_modal="$emit('close_modal')" />
		</div>
	</div>
</template>

<script setup lang="ts">
const playerDataStore = usePlayerDataStore()
const avgPercentTeamDamage = Number(playerDataStore.playerData?.sr.noxus_info.avg_team_damage_share.toFixed(2)) * 100 + '%'
const totalPhysicalDealt = playerDataStore.playerData?.sr.noxus_info.total_physical_damage_dealt_to_champions
const totalMagicDealt = playerDataStore.playerData?.sr.noxus_info.total_magic_damage_dealt_to_champions
const totalTrueDealt = playerDataStore.playerData?.sr.noxus_info.total_true_damage_dealt_to_champions
const avgKDA = Number(playerDataStore.playerData?.sr.noxus_info.avg_kda.toFixed(2))
const firstBloods = playerDataStore.playerData?.sr.noxus_info.total_first_bloods
const totalKills = playerDataStore.playerData?.sr.noxus_info.total_kills
const firstBloodPercentage = Math.round((firstBloods / totalKills) * 100)
const totalDoublekills = playerDataStore.playerData?.sr.noxus_info.total_double_kills
const totalTriplekills = playerDataStore.playerData?.sr.noxus_info.total_triple_kills
const totalQuadrakills = playerDataStore.playerData?.sr.noxus_info.total_quadra_kills
const totalPentakills = playerDataStore.playerData?.sr.noxus_info.total_penta_kills
const largestKillingSpree = playerDataStore.playerData?.sr.noxus_info.highest_largest_killing_spree

const noxusData = {
	backdropImage: "/region-backdrop/noxusbackdrop.png",
	title: "The noxus",
	description: "Strength Through Might and Conquest",
	bgColor: "bg-noxus-secondary",
	borderColor: "border-noxus-primary",
}

const noxusStats = {
	borderColor: "border-noxus-primary",
	stats: [
		{
			title: "Damage Dealt",
			value: null,
			showGraph: true,
			graphType: "pie",
			graphLabels: ["Physical", "Magic", "True"],
			graphData: [totalPhysicalDealt, totalMagicDealt, totalTrueDealt],
			graphColors: ["#c62828", "#1565c0", "#ffffff"],
		},
		{ title: "avg percentTeamDamage", value: avgPercentTeamDamage },
		{
			title: "First Bloods",
			value: null,
			showGraph: true,
			graphType: "doughnut",
			graphLabels: ["First Bloods", "Other Kills"],
			graphData: [firstBloods, totalKills - firstBloods],
			graphColors: ["#c62828", "#808080"],
		},
		{ title: "Average KDA", value: avgKDA },
		{
			title: "Multikills",
			value: { "Double kills": totalDoublekills, "Triple kills": totalTriplekills, "Quadra kills": totalQuadrakills, "Penta kills": totalPentakills },
		},
		{ title: "Largest Killing Spree", value: largestKillingSpree },
	],
}

const noxusAchievements = {
	bgColor: "bg-noxus-secondary",
	borderColor: "border-noxus-primary",
	sectionText: "YOUR ACHIEVEMENTS",
	achievementText: "Your longest game was on 11/2/2025, lasting 100 minutes. And yada YADA YADA",
}

const noxusContinue = {
	bgColor: "bg-noxus-secondary",
	borderColor: "border-noxus-primary",
	continueText: "YOU'VE PROVED YOUR STRENGTH",
	buttonText: "Continue Your Journey",
}
// network fetching
</script>
