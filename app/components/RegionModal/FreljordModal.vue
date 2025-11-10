<template>
	<div class="w-full h-full bg-freljord-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="freljordData" />
		<div class="px-4 sm:px-16">
			<SmallerRegionSharedCardCollector v-bind="freljordStats" />
			<SmallerRegionSharedAchievements v-bind="freljordAchievements" />
			<SmallerRegionSharedContinue v-bind="freljordContinue" @close_modal="$emit('close_modal')" />
		</div>
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
const totalPhysicalTaken = playerDataStore.playerData?.sr.freljord_info.total_physical_damage_taken
const totalMagicTaken = playerDataStore.playerData?.sr.freljord_info.total_magic_damage_taken
const totalTrueTaken = playerDataStore.playerData?.sr.freljord_info.total_true_damage_taken
const totalDamageTaken = (totalPhysicalTaken ?? 0) + (totalMagicTaken ?? 0) + (totalTrueTaken ?? 0)
const physicalPercentage = Math.round(((totalPhysicalTaken ?? 0) / totalDamageTaken) * 100)
const magicPercentage = Math.round(((totalMagicTaken ?? 0) / totalDamageTaken) * 100)
const truePercentage = Math.round(((totalTrueTaken ?? 0) / totalDamageTaken) * 100)
const damageSelfMitigated = playerDataStore.playerData?.sr.freljord_info.total_damage_self_mitigated
const totalHeal = playerDataStore.playerData?.sr.freljord_info.total_heal
const totalHealsOnTeammates = playerDataStore.playerData?.sr.freljord_info.total_heals_on_teammates
const avgSurvivalRatio = Number(playerDataStore.playerData?.sr.freljord_info.avg_survival_ratio.toFixed(2))
const timePlayed = playerDataStore.playerData?.sr.freljord_info.total_play_time

const hours = Math.floor(timePlayed / 60);
const minutes = timePlayed % 60;
const formattedTime = `${hours}h ${Number(minutes.toFixed(0))}m`;

const totalSnowballThrows = playerDataStore.playerData?.aram.freljord_info.total_snowball_throws
const freljordStats = {
	borderColor: "border-freljord-primary",
	stats: [
		{
			title: "Damage Taken",
			value: null,
			showGraph: true,
			graphType: "pie",
			graphLabels: ["Physical", "Magic", "True"],
			graphData: [physicalPercentage, magicPercentage, truePercentage],
			graphColors: ["#c62828", "#1565c0", "#ffffff"],
		},
		{ title: "damageSelfMitigated", value: damageSelfMitigated },
		{
			title: "Damage Healed",
			value: null,
			showGraph: true,
			graphType: "bar",
			graphLabels: ["Total healed", "Total healing to allies"],
			graphData: [totalHeal, totalHealsOnTeammates],
			graphColors: ["#c62828", "#008000"],
		},
		{ title: "Average Survival Ratio", value: avgSurvivalRatio },
		{ title: "Time Played", value: formattedTime },
		{ title: "Total Snowball Throws", value: totalSnowballThrows ?? 0 },
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
	continueText: "YOU'VE ENDURED THE FROST",
	buttonText: "Continue Your Journey",
}
// network fetching
</script>
