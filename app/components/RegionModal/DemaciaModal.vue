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
const audio = ref()

onMounted(() => {
    audio.value = new Audio("soundfiles/region_music/demaciaIntro.mp3")
    audio.value.loop = true
    audio.value.volume = 0.5
    audio.value.play()
})

onBeforeUnmount(() => {
    if (audio.value) {
        audio.value.pause()
        audio.value.currentTime = 0
    }
})
</script>
