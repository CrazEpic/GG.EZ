<template>
	<div class="flex absolute top-0 left-0 w-full h-full bg-targon-secondary font-cinzel text-center">
		<!-- <RegionOverlayTitle v-bind="targonData" /> -->
		<ChampionConstellation champion="Aatrox" class="grow"></ChampionConstellation>
		<!-- <Continue class="absolute top-0.5 bottom-20" v-bind="targonContinue" @close_modal="$emit('close_modal')" /> -->
		<button :class="`absolute left-1/2 bottom-2 -translate-x-1/2 bg-black border-2 px-10 py-1 w-64 h-16 ${targonContinue.bgColor} text-white cursor-pointer mb-20`" @click="$emit('close_modal')">
			{{ targonContinue.continueText }}
		</button>
	</div>
</template>

<script setup lang="ts">
const targonData = {
	backdropImage: "/region-backdrop/targonbackdrop.png",
	title: "Targon",
	description: "REAPLCE ME",
	bgColor: "bg-targon-secondary",
	borderColor: "border-targon-primary",
}

const targonContinue = {
	bgColor: "bg-targon-secondary",
	borderColor: "border-targon-primary",
	continueText: "Continue Your Journey",
	buttonText: "REPLACE ME",
}
</script>
