<template>
	<div class="w-full h-full bg-freljord-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="freljordData" />
		<SmallerRegionSharedCardCollector v-bind="freljordStats" />
		<SmallerRegionSharedAchievements v-bind="freljordAchievements" />
		<SmallerRegionSharedContinue v-bind="freljordContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">

const freljordData = {
	backdropImage: "/region-backdrop/freljordbackdrop.png",
	title: "The Freljord",
	description: "Survival Through Unity and Strength",
	bgColor: "bg-freljord-secondary",
	borderColor: "border-freljord-primary",
}

const freljordStats = {
	borderColor: 'border-freljord-primary',
    stats: [
		{title: 'Damage Taken', value: 'Total (physical, magic, true)'},
		{title: '% of Team Damage Soaked', value: 'Average'},
		{title: 'damageSelfMitigated', value: 'total'},
		{title: 'totalHeal', value: 'Total, totalHealsOnTeammates → Total'},
		{title: 'avg survivalRatio', value: '1:2'},
		{title: 'max timePlayed', value: '100 mins'},
	]
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
