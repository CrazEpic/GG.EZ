<template>
	<div class="w-full h-full bg-demacia-secondary font-cinzel text-center">
		<RegionOverlayTitle v-bind="demaciaData" />
		<Continue v-bind="demaciaContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">
import RegionOverlayTitle from "./RegionOverlayTitle.vue"
import Continue from "./Continue.vue"

const demaciaData = {
	backdropImage: "/region-backdrop/demaciabackdrop.png",
	title: "The demacia",
	description: "Survival Through Unity and Strength",
	bgColor: "bg-demacia-secondary",
	borderColor: "border-demacia-primary",
}

const demaciaContinue = {
	bgColor: 'bg-demacia-secondary',
    borderColor : 'border-demacia-primary',
    continueText: "YOU'VE ENDURED THE FROST",
    buttonText: 'Continue Your Journey',
}
// network fetching
</script>
