<template>
	<div class="w-full h-full bg-demacia-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="demaciaData" />

		<div class="px-4 sm:px-16">
			<DemaciaPostcard></DemaciaPostcard>
			<SmallerRegionSharedContinue v-bind="demaciaContinue" @close_modal="$emit('close_modal')" />
		</div>
	</div>
</template>

<script setup lang="ts">
const demaciaData = {
	backdropImage: "/region-backdrop/demaciabackdrop.png",
	title: "The demacia",
	description: "Survival Through Unity and Strength",
	bgColor: "bg-demacia-secondary",
	borderColor: "border-demacia-primary",
}

const demaciaContinue = {
	bgColor: "bg-demacia-secondary",
	borderColor: "border-demacia-primary",
	continueText: "YOU'VE ENDURED THE FROST",
	buttonText: "Continue Your Journey",
}
</script>
