<template>
	<div class="w-full h-full bg-ixtal-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="ixtalData" />
		<SmallerRegionSharedCardCollector v-bind="ixtalStats" />
		<SmallerRegionSharedAchievements v-bind="ixtalAchievements" />
		<SmallerRegionSharedContinue v-bind="ixtalContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">

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
		{title: 'avg visionScorePerMinute', values: 'average'},
		{title: 'total pings', values: 'number'},
		{title: 'total objectivesStolen', values: 'total'},
		{title: 'avg JungleShare (as jungler)', values: 'avg'},
		{title: 'total wards killed', values: 'number'},
		{title: 'total wards placed', values: 'number'},
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
