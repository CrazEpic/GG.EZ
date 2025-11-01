<template>
	<div class="flex flex-col relative">
		<LandingScreen v-if="modalType == 'LANDING_SCREEN'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10"></LandingScreen>
		<FreljordModal v-if="modalType == 'FRELJORD'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10"></FreljordModal>
		<MapCanvas @change_modal="(modal) => {modalType = modal}" class="grow"></MapCanvas>
	</div>
</template>

<script setup lang="ts">
const modalType = ref("LANDING_SCREEN")
const pixi = usePixiStore()

const closeModal = async () => {
	await pixi.resetCamera()
	modalType.value = "None"
}
</script>
