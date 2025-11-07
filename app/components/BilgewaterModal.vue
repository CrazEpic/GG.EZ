<template>
	<div class="w-full h-full bg-bilgewater-secondary font-cinzel text-center">
		<RegionOverlayTitle v-bind="bilgewaterData" />
		<CardCollector v-bind="bilgewaterStats" />
		<Achievements v-bind="bilgewaterAchievements" />
		<Continue v-bind="bilgewaterContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">
import RegionOverlayTitle from "./RegionOverlayTitle.vue"
import CardCollector from "./CardCollector.vue"
import Achievements from "./Achievements.vue"
import Continue from "./Continue.vue"

const bilgewaterData = {
	backdropImage: "/region-backdrop/bilgewaterbackdrop.png",
	title: "The bilgewater",
	description: "Survival Through Unity and Strength",
	bgColor: "bg-bilgewater-secondary",
	borderColor: "border-bilgewater-primary",
}

const bilgewaterStats = {
	borderColor: 'border-bilgewater-primary',
    stats: [
		{title: 'Damage Taken', value: 'Total (physical, magic, true)'},
		{title: '% of Team Damage Soaked', value: 'Average'},
		{title: 'damageSelfMitigated', value: 'total'},
		{title: 'totalHeal', value: 'Total, totalHealsOnTeammates → Total'},
		{title: 'avg survivalRatio', value: '1:2'},
		{title: 'max timePlayed', value: '100 mins'},
	]
}

const bilgewaterAchievements = {
	bgColor: 'bg-bilgewater-secondary',
    borderColor : 'border-bilgewater-primary',
    sectionText : 'YOUR ACHIEVEMENTS',
    achievementText: 'Your longest game was on 11/2/2025, lasting 100 minutes. And yada YADA YADA',
}

const bilgewaterContinue = {
	bgColor: 'bg-bilgewater-secondary',
    borderColor : 'border-bilgewater-primary',
    continueText: 'YOU ENDURED THE FROST',
    buttonText: 'Continue Your Journey',
}
// network fetching
</script>
