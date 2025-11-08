<template>
	<div class="w-full h-full bg-shadowIsles-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="shadowIslesData" />
		<SmallerRegionSharedCardCollector v-bind="shadowIslesStats" />
		<SmallerRegionSharedAchievements v-bind="shadowIslesAchievements" />
		<SmallerRegionSharedContinue v-bind="shadowIslesContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">

const shadowIslesData = {
	backdropImage: "/region-backdrop/shadowIslesbackdrop.png",
	title: "The shadowIsles",
	description: "Tenacity Forged in the Black Mist",
	bgColor: "bg-shadowIsles-secondary",
	borderColor: "border-shadowIsles-primary",
}

const shadowIslesStats = {
	borderColor: 'border-shadowIsles-primary',
    stats: [
		{title: 'total deaths + totalTimeSpentDead', value: 'number'},
		{title: 'death ratio', value: 'ratio'},
		{title: 'death heatmap', value: '?'},
		{title: 'gameEndedInSurrender', value: 'number'},
		{title: 'maxDeathsInSingleGame', value: '30'},
		{title: 'total revenge kills', value: 'number'},
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
    continueText: "YOU'VE SURVIVED THE HARROWING",
    buttonText: 'Continue Your Journey',
}
// network fetching
</script>
