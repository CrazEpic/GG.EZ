<template>
	<div class="w-full h-full bg-ixtal-secondary font-cinzel text-center">
		<RegionOverlayTitle v-bind="ixtalData" />
		<CardCollector v-bind="ixtalStats" />
		<Achievements v-bind="ixtalAchievements" />
		<Continue v-bind="ixtalContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">
import RegionOverlayTitle from "./RegionOverlayTitle.vue"
import CardCollector from "./CardCollector.vue"
import Achievements from "./Achievements.vue"
import Continue from "./Continue.vue"

const ixtalData = {
	backdropImage: "/region-backdrop/ixtalbackdrop.png",
	title: "The ixtal",
	description: "Survival Through Unity and Strength",
	bgColor: "bg-ixtal-secondary",
	borderColor: "border-ixtal-primary",
}

const ixtalStats = {
	borderColor: 'border-ixtal-primary',
    stats: [
		{title: 'Damage Taken', value: 'Total (physical, magic, true)'},
		{title: '% of Team Damage Soaked', value: 'Average'},
		{title: 'damageSelfMitigated', value: 'total'},
		{title: 'totalHeal', value: 'Total, totalHealsOnTeammates → Total'},
		{title: 'avg survivalRatio', value: '1:2'},
		{title: 'max timePlayed', value: '100 mins'},
	]
}

const ixtalAchievements = {
	bgColor: 'bg-ixtal-secondary',
    borderColor : 'border-ixtal-primary',
    sectionText : 'YOUR ACHIEVEMENTS',
    achievementText: 'Your longest game was on 11/2/2025, lasting 100 minutes. And yada YADA YADA',
}

const ixtalContinue = {
	bgColor: 'bg-ixtal-secondary',
    borderColor : 'border-ixtal-primary',
    continueText: 'YOU ENDURED THE FROST',
    buttonText: 'Continue Your Journey',
}
// network fetching
</script>
