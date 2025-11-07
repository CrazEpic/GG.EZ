<template>
	<div class="flex flex-col relative">
		<LandingScreen v-if="modalType == 'LANDING_SCREEN'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10"></LandingScreen>
		<FreljordModal v-if="modalType == 'FRELJORD'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10"></FreljordModal>
		<NoxusModal v-if="modalType == 'NOXUS'" @close_modal="closeModal"
		class="absolute top-0 left-0 w-full h-full z-10"></NoxusModal>
		<IoniaModel v-if="modalType == 'IONIA'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10"></IoniaModel>
		<BilgewaterModal v-if="modalType == 'BILGEWATER'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10"></BilgewaterModal>
		<ShadowIslesModal v-if="modalType == 'SHADOW_ISLES'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10"></ShadowIslesModal>
		<IxtalModal v-if="modalType == 'IXTAL'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10"></IxtalModal>
		<ShurimaModal v-if="modalType == 'SHURIMA'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10"></ShurimaModal>
		<TargonModal v-if="modalType == 'TARGON'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10"></TargonModal>
		<DemaciaModal v-if="modalType == 'DEMACIA'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10"></DemaciaModal>
		<MapCanvas
			@change_modal="
				(modal) => {
					modalType = modal
				}
			"
			class="grow"
		></MapCanvas>
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
