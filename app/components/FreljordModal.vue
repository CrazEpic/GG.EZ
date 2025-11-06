<template>
	<div class="w-full h-full bg-freljord-secondary font-cinzel text-center">
		<RegionOverlayTitle v-bind="freljordData" />
		<CardCollector v-bind="freljordStats" />
		<Achievements v-bind="freljordAchievements" />
		<Continue v-bind="freljordContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">
import RegionOverlayTitle from "./RegionOverlayTitle.vue"
import CardCollector from "./CardCollector.vue"
import Achievements from "./Achievements.vue"
import Continue from "./Continue.vue"

const freljordData = {
	backdropImage: "/region-backdrop/freljordbackdrop.jpg",
	title: "The Freljord",
	description: "Survival Through Unity and Strength",
	bgColor: "bg-freljord-secondary",
	borderColor: "border-freljord-primary",
}

const freljordStats = {
	borderColor: 'border-freljord-primary',
    stat1: 'damageTaken → Total (physical, magic, true)',
    stat2: '% of Team Damage Soaked → Average',
    stat3: 'damageSelfMitigated → total',
    stat4: 'totalHeal → Total, totalHealsOnTeammates → Total',
    stat5: 'avg survivalRatio',
	stat6: 'max timePlayed',
}

const freljordAchievements = {
	bgColor: 'bg-freljord-secondary',
    borderColor : 'border-freljord-primary',
    sectionText : 'YOUR ACHIEVEMENTS',
    achievementText: 'Your longest game was on 11/2/2025, lasting 100 minutes. And yada YADA YADA',
}

const freljordContinue = {
	bgColor: 'bg-freljord-secondary',
    borderColor : 'border-freljord-primary',
    continueText: 'YOU ENDURED THE FROST',
    buttonText: 'Continue Your Journey',
}
// network fetching
</script>
