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
	description: "Reclaim Legacy Through Structure and Dominion",
	bgColor: "bg-shurima-secondary",
	borderColor: "border-shurima-primary",
}

const shurimaStats = {
	borderColor: 'border-shurima-primary',
    stats: [
		{title: 'total turretKills', value: 'Total'},
		{title: 'dragonKills, baronKills, atakahn, rifthereald', value: 'Number'},
		{title: 'avg ObjectiveParticipation (so structures and jungle bosses)', value: 'avg'},
		{title: 'firstTowerKill, firstDragon, firstBaron, firstRiftHerald', value: 'num'},
		{title: 'total damageDealtToObjectives', value: 'total'},
		{title: 'total damageDealtToStructures', value: 'total'},
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
    continueText: "YOU'VE EARNED YOUR ASCENSION",
    buttonText: 'Continue Your Journey',
}
// network fetching
</script>
