<template>
	<div class="w-full h-full bg-noxus-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="noxusData" />
		<SmallerRegionSharedCardCollector v-bind="noxusStats" />
		<SmallerRegionSharedAchievements v-bind="noxusAchievements" />
		<SmallerRegionSharedContinue v-bind="noxusContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">
const noxusData = {
	backdropImage: "/region-backdrop/noxusbackdrop.png",
	title: "The noxus",
	description: "Strength Through Might and Conquest",
	bgColor: "bg-noxus-secondary",
	borderColor: "border-noxus-primary",
}

const noxusStats = {
	borderColor: 'border-noxus-primary',
    stats: [
		{title: 'totalDamageDealt', value: '(physical, magic, true)'},
		{title: 'avg percentTeamDamage', value: '%'},
		{title: 'first bloodkill %+ total kills + assist', value: '% number'},
		{title: 'avg kda', value: '3.0'},
		{title: 'total double + triple + quadra + pentakills', value: '1,2,3,4'},
		{title: 'largestKillingSpree', value: '30'},
	]
}

const noxusAchievements = {
	bgColor: 'bg-noxus-secondary',
    borderColor : 'border-noxus-primary',
    sectionText : 'YOUR ACHIEVEMENTS',
    achievementText: 'Your longest game was on 11/2/2025, lasting 100 minutes. And yada YADA YADA',
}

const noxusContinue = {
	bgColor: 'bg-noxus-secondary',
    borderColor : 'border-noxus-primary',
    continueText: "YOU'VE PROVED YOUR STRENGTH",
    buttonText: 'Continue Your Journey',
}
// network fetching
</script>
