<template>
	<div class="w-full h-full bg-noxus-secondary font-cinzel text-center">
		<RegionOverlayTitle v-bind="noxusData" />
		<CardCollector v-bind="noxusStats" />
		<Achievements v-bind="noxusAchievements" />
		<Continue v-bind="noxusContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">
import RegionOverlayTitle from "./RegionOverlayTitle.vue"
import CardCollector from "./CardCollector.vue"
import Achievements from "./Achievements.vue"
import Continue from "./Continue.vue"

const noxusData = {
	backdropImage: "/region-backdrop/noxusbackdrop.png",
	title: "The noxus",
	description: "Survival Through Unity and Strength",
	bgColor: "bg-noxus-secondary",
	borderColor: "border-noxus-primary",
}

const noxusStats = {
	borderColor: 'border-noxus-primary',
    stats: [
		{title: 'Damage Taken', value: 'Total (physical, magic, true)'},
		{title: '% of Team Damage Soaked', value: 'Average'},
		{title: 'damageSelfMitigated', value: 'total'},
		{title: 'totalHeal', value: 'Total, totalHealsOnTeammates → Total'},
		{title: 'avg survivalRatio', value: '1:2'},
		{title: 'max timePlayed', value: '100 mins'},
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
    continueText: 'YOU ENDURED THE FROST',
    buttonText: 'Continue Your Journey',
}
// network fetching
</script>
