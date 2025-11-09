<template>
	<div class="w-full h-full bg-bilgewater-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="bilgewaterData" />
		<SmallerRegionSharedCardCollector v-bind="bilgewaterStats" />
		<SmallerRegionSharedAchievements v-bind="bilgewaterAchievements" />
		<SmallerRegionSharedContinue v-bind="bilgewaterContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">

const bilgewaterData = {
	backdropImage: "/region-backdrop/bilgewaterbackdrop.png",
	title: "The bilgewater",
	description: "Fortune Favors the Bold",
	bgColor: "bg-bilgewater-secondary",
	borderColor: "border-bilgewater-primary",
}

const bilgewaterStats = {
	borderColor: 'border-bilgewater-primary',
    stats: [
		{title: 'total goldEarned', values: 'number'},
		{title: 'top items', values: 'items'},
		{title: 'avg cs per minute', values: 'number'},
		{title: 'total shutdownBounty', values: 'number'},
		{title: 'most gold in a single match', values: 'number'},
		{title: 'most cs in a single match', values: 'number'},
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
    continueText: "YOU'VE SEIZED YOUR FORTUNE",
    buttonText: 'Continue Your Journey',
}
// network fetching
</script>
