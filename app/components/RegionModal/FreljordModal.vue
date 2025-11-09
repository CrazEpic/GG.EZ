<template>
	<div class="w-full h-full bg-freljord-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="freljordData" />
		<SmallerRegionSharedCardCollector v-bind="freljordStats" />
		<SmallerRegionSharedAchievements v-bind="freljordAchievements" />
		<SmallerRegionSharedContinue v-bind="freljordContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">
const freljordData = {
	backdropImage: "/region-backdrop/freljordbackdrop.png",
	title: "The Freljord",
	description: "Survival Through Unity and Strength",
	bgColor: "bg-freljord-secondary",
	borderColor: "border-freljord-primary",
}

const playerDataStore = usePlayerDataStore()
const damageSelfMitigated = playerDataStore.playerData?.sr.freljord_info.total_damage_self_mitigated
const totalPhysicalTaken = playerDataStore.playerData?.sr.freljord_info.total_physical_damage_taken
const totalMagicTaken = playerDataStore.playerData?.sr.freljord_info.total_magic_damage_taken
const totalTrueTaken = playerDataStore.playerData?.sr.freljord_info.total_true_damage_taken
const totalHeal = playerDataStore.playerData?.sr.freljord_info.total_heal
const totalHealsOnTeammates = playerDataStore.playerData?.sr.freljord_info.total_heals_on_teammates
const avgSurvivalRatio = playerDataStore.playerData?.sr.freljord_info.avg_survival_ratio
const timePlayed = playerDataStore.playerData?.sr.freljord_info.total_play_time
const totalSnowballThrows = playerDataStore.playerData?.aram.freljord_info.total_snowball_throws
const freljordStats = {
	borderColor: "border-freljord-primary",
	stats: [
		{ 
		title: "Damage Taken", 
		values: { physical: totalPhysicalTaken, magic: totalMagicTaken, true: totalTrueTaken },
		showGraph: true
		},
		{ title: "damageSelfMitigated", values: damageSelfMitigated },
		{ title: "totalHeal", values: { "total healing": totalHeal, "heals on teammates": totalHealsOnTeammates } },
		{ title: "avg survivalRatio", values: avgSurvivalRatio },
		{ title: "max timePlayed", values: timePlayed },
		{ title: "total snowball throws", values: totalSnowballThrows ?? 0 },
	],
}

const freljordAchievements = {
	bgColor: "bg-freljord-secondary",
	borderColor: "border-freljord-primary",
	sectionText: "YOUR ACHIEVEMENTS",
	achievementText: "Your longest game was on 11/2/2025, lasting 100 minutes. And yada YADA YADA",
}

const freljordContinue = {
	bgColor: "bg-freljord-secondary",
	borderColor: "border-freljord-primary",
	continueText: "YOU ENDURED THE FROST",
	buttonText: "Continue Your Journey",
}
// network fetching
</script>
