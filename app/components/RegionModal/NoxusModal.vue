<template>
	<div class="w-full h-full bg-noxus-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="noxusData" />
		<SmallerRegionSharedCardCollector v-bind="noxusStats" />
		<SmallerRegionSharedAchievements v-bind="noxusAchievements" />
		<SmallerRegionSharedContinue v-bind="noxusContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">
const playerDataStore = usePlayerDataStore()
const avgPercentTeamDamage = playerDataStore.playerData?.sr.noxus_info.avg_team_damage_share
const avgKDA = playerDataStore.playerData?.sr.noxus_info.avg_kda
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
	borderColor: 'border-noxus-primary',
    stats: [
		{title: 'totalDamageDealt', values: '(physical, magic, true)'},
		{title: 'avg percentTeamDamage', values: avgPercentTeamDamage},
		{title: 'first bloodkill %+ total kills + assist', values: '% number'},
		{title: 'avg kda', values: avgKDA},
		{title: 'Multikills', values: {'Double kills': totalDoublekills, 'Triple kills': totalTriplekills, 'Quadra kills': totalQuadrakills, 'Penta kills': totalPentakills}},
		{title: 'largestKillingSpree', values: largestKillingSpree},
	]
}

const noxusAchievements = {
	bgColor: 'bg-noxus-secondary',
    borderColor : 'border-noxus-primary',
    sectionText : 'YOUR ACHIEVEMENTS',
    achievementText: 'Your longest game was on 11/2/2025, lasting 100 minutes. And yada YADA YADA',
}

const noxusContinue = {
	bgColor: 'bg-noxus-secondary',
    borderColor : 'border-noxus-primary',
    continueText: "YOU'VE PROVED YOUR STRENGTH",
    buttonText: 'Continue Your Journey',
}
// network fetching
</script>
