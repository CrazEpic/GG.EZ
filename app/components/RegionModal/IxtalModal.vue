<template>
	<div class="w-full h-full bg-ixtal-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="ixtalData" />
		<div class="px-4 sm:px-16">
			<SmallerRegionSharedCardCollector v-bind="ixtalStats" />
			<SmallerRegionSharedAchievements v-bind="ixtalAchievements" />
			<SmallerRegionSharedContinue v-bind="ixtalContinue" @close_modal="$emit('close_modal')" />
		</div>
	</div>
</template>

<script setup lang="ts">
const playerDataStore = usePlayerDataStore()
const ixtalInfo = playerDataStore.playerData?.sr.ixtal_info
const avgVisionScorePerMin = Number(playerDataStore.playerData?.sr.ixtal_info.avg_vision_score_per_min.toFixed(2))
const totalPings = ixtalInfo
	? Object.entries(ixtalInfo)
			.filter(([key, value]) => key.endsWith("Pings"))
			.reduce((sum, [key, value]) => sum + value, 0)
	: 0
const totalObjStolen = playerDataStore.playerData?.sr.ixtal_info.total_objectives_stolen
const avgJungleShare = Number(playerDataStore.playerData?.sr.ixtal_info.avg_jungle_share_when_jungle.toFixed(2))
const wardsKilled = playerDataStore.playerData?.sr.ixtal_info.total_total_wards_killed
const wardsPlaced = playerDataStore.playerData?.sr.ixtal_info.total_total_wards_placed

const ixtalData = {
	backdropImage: "/region-backdrop/ixtalbackdrop.png",
	title: "The ixtal",
	description: "Where Sight Pierces the Jungle's Veil",
	bgColor: "bg-ixtal-secondary",
	borderColor: "border-ixtal-primary",
}

const ixtalStats = {
	borderColor: "border-ixtal-primary",
	stats: [
		{ title: "Average Vision Score per Minute", value: avgVisionScorePerMin },
		{ title: "Total Pings", value: totalPings },
		{ title: "Total Objectives Stolen", value: totalObjStolen },
		{ title: "Average Jungle Share", value: avgJungleShare },
		{ title: "Total Wards Killed", value: wardsKilled },
		{ title: "Total Wards Placed", value: wardsPlaced },
	],
}

const ixtalAchievements = {
	bgColor: "bg-ixtal-secondary",
	borderColor: "border-ixtal-primary",
	sectionText: "The Rift Report",
	achievementText: playerDataStore.playerData?.llm_responses.sr.ixtal_response,
}

const ixtalContinue = {
	bgColor: "bg-ixtal-secondary",
	borderColor: "border-ixtal-primary",
	continueText: "YOU'VE MASTERED THE WILDERNESS",
	buttonText: "Continue Your Journey",
}
// network fetching
const audio = ref()

onMounted(() => {
    audio.value = new Audio("soundfiles/region_music/ixtal.mp3")
    audio.value.loop = true
    audio.value.volume = 0.5
    audio.value.play()
})

onBeforeUnmount(() => {
    if (audio.value) {
        audio.value.pause()
        audio.value.currentTime = 0
    }
})
</script>
