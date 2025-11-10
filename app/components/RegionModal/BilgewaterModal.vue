<template>
	<div class="w-full h-full bg-bilgewater-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="bilgewaterData" />
		<div class="px-4 sm:px-16">
			<SmallerRegionSharedCardCollector v-bind="bilgewaterStats" />
			<SmallerRegionSharedAchievements v-bind="bilgewaterAchievements" />
			<SmallerRegionSharedContinue v-bind="bilgewaterContinue" @close_modal="$emit('close_modal')" />
		</div>
	</div>
</template>

<script setup lang="ts">
const playerDataStore = usePlayerDataStore()

const totalGoldEarned =  useSessionStore().displaySR ? playerDataStore.playerData?.sr.bilgewater_info.total_gold_earned : playerDataStore.playerData?.aram.bilgewater_info.total_gold_earned
const topItemsPurchased = useSessionStore().displaySR ? playerDataStore.playerData?.sr.bilgewater_info.top_3_items : playerDataStore.playerData?.aram.bilgewater_info.top_3_items
const avgCSPerMinute = Number(useSessionStore().displaySR ? playerDataStore.playerData?.sr.bilgewater_info.avg_cs_per_min.toFixed(2) : playerDataStore.playerData?.aram.bilgewater_info.avg_cs_per_min.toFixed(2))
const totalShutdownBounty = useSessionStore().displaySR ? playerDataStore.playerData?.sr.bilgewater_info.total_shutdown_bounty : playerDataStore.playerData?.aram.bilgewater_info.total_shutdown_bounty
const highest_shutdown_bounty = useSessionStore().displaySR ? playerDataStore.playerData?.sr.bilgewater_info.highest_shutdown_bounty : playerDataStore.playerData?.aram.bilgewater_info.highest_shutdown_bounty
const mostGoldSingleMatch = useSessionStore().displaySR ? playerDataStore.playerData?.sr.bilgewater_info.most_gold_in_single_game : playerDataStore.playerData?.aram.bilgewater_info.most_gold_in_single_game
const mostCSSingleMatch = useSessionStore().displaySR ? playerDataStore.playerData?.sr.bilgewater_info.most_cs_in_single_game : playerDataStore.playerData?.aram.bilgewater_info.most_cs_in_single_game

const bilgewaterData = {
	backdropImage: "/region-backdrop/bilgewaterbackdrop.png",
	title: "The bilgewater",
	description: "Fortune Favors the Bold",
	bgColor: "bg-bilgewater-secondary",
	borderColor: "border-bilgewater-primary",
}

const bilgewaterStats = {
	borderColor: "border-bilgewater-primary",
	stats: [
		{ title: "Total Gold Earned", value: totalGoldEarned + "g" },
		{ title: "Top Items Purchased", topItems: topItemsPurchased },
		{ title: "Average CS Per Minute", value: avgCSPerMinute },
		{ title: "Total Shutdown Bounty", value: totalShutdownBounty },
		{ title: "Highest ShutdownBounty", value: highest_shutdown_bounty },
		{ title: "Most Gold in a Single Match", value: mostGoldSingleMatch },
		{ title: "Most CS in a Single Match", value: mostCSSingleMatch },
	],
}

const bilgewaterAchievements = {
	bgColor: "bg-bilgewater-secondary",
	borderColor: "border-bilgewater-primary",
	sectionText: "The Rift Report",
	achievementText: useSessionStore().displaySR ? playerDataStore.playerData?.llm_responses.sr.bilgewater_response : playerDataStore.playerData?.llm_responses.aram.bilgewater_response,
}

const bilgewaterContinue = {
	bgColor: "bg-bilgewater-secondary",
	borderColor: "border-bilgewater-primary",
	continueText: "YOU'VE SEIZED YOUR FORTUNE",
	buttonText: "Continue Your Journey",
}
// network fetching

const audio = ref()

onMounted(() => {
	audio.value = new Audio("soundfiles/region_music/bilgewater.mp3")
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
