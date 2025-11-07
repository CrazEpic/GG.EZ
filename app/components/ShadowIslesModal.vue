<template>
	<div class="w-full h-full bg-shadowIsles-secondary font-cinzel text-center">
		<RegionOverlayTitle v-bind="shadowIslesData" />
		<CardCollector v-bind="shadowIslesStats" />
		<Achievements v-bind="shadowIslesAchievements" />
		<Continue v-bind="shadowIslesContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">
import RegionOverlayTitle from "./RegionOverlayTitle.vue"
import CardCollector from "./CardCollector.vue"
import Achievements from "./Achievements.vue"
import Continue from "./Continue.vue"

const shadowIslesData = {
	backdropImage: "/region-backdrop/shadowIslesbackdrop.png",
	title: "The shadowIsles",
	description: "Survival Through Unity and Strength",
	bgColor: "bg-shadowIsles-secondary",
	borderColor: "border-shadowIsles-primary",
}

const shadowIslesStats = {
	borderColor: 'border-shadowIsles-primary',
    stats: [
		{title: 'Damage Taken', value: 'Total (physical, magic, true)'},
		{title: '% of Team Damage Soaked', value: 'Average'},
		{title: 'damageSelfMitigated', value: 'total'},
		{title: 'totalHeal', value: 'Total, totalHealsOnTeammates → Total'},
		{title: 'avg survivalRatio', value: '1:2'},
		{title: 'max timePlayed', value: '100 mins'},
	]
}

const shadowIslesAchievements = {
	bgColor: 'bg-shadowIsles-secondary',
    borderColor : 'border-shadowIsles-primary',
    sectionText : 'YOUR ACHIEVEMENTS',
    achievementText: 'Your longest game was on 11/2/2025, lasting 100 minutes. And yada YADA YADA',
}

const shadowIslesContinue = {
	bgColor: 'bg-shadowIsles-secondary',
    borderColor : 'border-shadowIsles-primary',
    continueText: 'YOU ENDURED THE FROST',
    buttonText: 'Continue Your Journey',
}
// network fetching
</script>
