<template>
	<div class="w-full h-full bg-shurima-secondary font-cinzel text-center">
		<RegionOverlayTitle v-bind="shurimaData" />
		<CardCollector v-bind="shurimaStats" />
		<Achievements v-bind="shurimaAchievements" />
		<Continue v-bind="shurimaContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">
import RegionOverlayTitle from "./RegionOverlayTitle.vue"
import CardCollector from "./CardCollector.vue"
import Achievements from "./Achievements.vue"
import Continue from "./Continue.vue"

const shurimaData = {
	backdropImage: "/region-backdrop/shurimabackdrop.png",
	title: "The shurima",
	description: "Survival Through Unity and Strength",
	bgColor: "bg-shurima-secondary",
	borderColor: "border-shurima-primary",
}

const shurimaStats = {
	borderColor: 'border-shurima-primary',
    stats: [
		{title: 'Damage Taken', value: 'Total (physical, magic, true)'},
		{title: '% of Team Damage Soaked', value: 'Average'},
		{title: 'damageSelfMitigated', value: 'total'},
		{title: 'totalHeal', value: 'Total, totalHealsOnTeammates → Total'},
		{title: 'avg survivalRatio', value: '1:2'},
		{title: 'max timePlayed', value: '100 mins'},
	]
}

const shurimaAchievements = {
	bgColor: 'bg-shurima-secondary',
    borderColor : 'border-shurima-primary',
    sectionText : 'YOUR ACHIEVEMENTS',
    achievementText: 'Your longest game was on 11/2/2025, lasting 100 minutes. And yada YADA YADA',
}

const shurimaContinue = {
	bgColor: 'bg-shurima-secondary',
    borderColor : 'border-shurima-primary',
    continueText: 'YOU ENDURED THE FROST',
    buttonText: 'Continue Your Journey',
}
// network fetching
</script>
