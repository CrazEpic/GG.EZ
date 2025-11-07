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
	description: "Where Sight Pierces the Jungle's Veil",
	bgColor: "bg-ixtal-secondary",
	borderColor: "border-ixtal-primary",
}

const ixtalStats = {
	borderColor: 'border-ixtal-primary',
    stats: [
		{title: 'avg visionScorePerMinute', value: 'average'},
		{title: 'total pings', value: 'number'},
		{title: 'total objectivesStolen', value: 'total'},
		{title: 'avg JungleShare (as jungler)', value: 'avg'},
		{title: 'total wards killed', value: 'number'},
		{title: 'total wards placed', value: 'number'},
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
    continueText: "YOU'VE MASTERED THE WILDERNESS",
    buttonText: 'Continue Your Journey',
}
// network fetching
</script>
