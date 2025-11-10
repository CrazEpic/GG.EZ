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
const avgPercentTeamDamage = useSessionStore().displaySR ? Number(playerDataStore.playerData?.sr.noxus_info.avg_team_damage_share.toFixed(2)) * 100 + '%' : Number(playerDataStore.playerData?.aram.noxus_info.avg_team_damage_share.toFixed(2)) * 100 + '%'
const totalPhysicalDealt = useSessionStore().displaySR ? playerDataStore.playerData?.sr.noxus_info.total_physical_damage_dealt_to_champions : playerDataStore.playerData?.aram.noxus_info.total_physical_damage_dealt_to_champions
const totalMagicDealt = useSessionStore().displaySR ? playerDataStore.playerData?.sr.noxus_info.total_magic_damage_dealt_to_champions : playerDataStore.playerData?.aram.noxus_info.total_magic_damage_dealt_to_champions
const totalTrueDealt = useSessionStore().displaySR ? playerDataStore.playerData?.sr.noxus_info.total_true_damage_dealt_to_champions : playerDataStore.playerData?.aram.noxus_info.total_true_damage_dealt_to_champions
const avgKDA = Number(useSessionStore().displaySR ? playerDataStore.playerData?.sr.noxus_info.avg_kda.toFixed(2) : playerDataStore.playerData?.aram.noxus_info.avg_kda.toFixed(2))
const firstBloods = useSessionStore().displaySR ? playerDataStore.playerData?.sr.noxus_info.total_first_bloods : playerDataStore.playerData?.aram.noxus_info.total_first_bloods
const totalKills = useSessionStore().displaySR ? playerDataStore.playerData?.sr.noxus_info.total_kills : playerDataStore.playerData?.aram.noxus_info.total_kills
const firstBloodPercentage = Math.round((firstBloods / totalKills) * 100)
const totalDoublekills = useSessionStore().displaySR ? playerDataStore.playerData?.sr.noxus_info.total_double_kills : playerDataStore.playerData?.aram.noxus_info.total_double_kills
const totalTriplekills = useSessionStore().displaySR ? playerDataStore.playerData?.sr.noxus_info.total_triple_kills : playerDataStore.playerData?.aram.noxus_info.total_triple_kills
const totalQuadrakills = useSessionStore().displaySR ? playerDataStore.playerData?.sr.noxus_info.total_quadra_kills : playerDataStore.playerData?.aram.noxus_info.total_quadra_kills
const totalPentakills = useSessionStore().displaySR ? playerDataStore.playerData?.sr.noxus_info.total_penta_kills : playerDataStore.playerData?.aram.noxus_info.total_penta_kills
const largestKillingSpree = useSessionStore().displaySR ? playerDataStore.playerData?.sr.noxus_info.highest_largest_killing_spree : playerDataStore.playerData?.aram.noxus_info.highest_largest_killing_spree

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
	sectionText: "The Rift Report",
	achievementText: useSessionStore().displaySR ? playerDataStore.playerData?.llm_responses.sr.noxus_response : playerDataStore.playerData?.llm_responses.aram.noxus_response,
}

const noxusContinue = {
	bgColor: "bg-noxus-secondary",
	borderColor: "border-noxus-primary",
	continueText: "YOU'VE PROVED YOUR STRENGTH",
	buttonText: "Continue Your Journey",
}
// network fetching
const audio = ref()

onMounted(() => {
	audio.value = new Audio("soundfiles/region_music/noxusIntro.mp3")
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
