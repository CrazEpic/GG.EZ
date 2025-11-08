<template>
	<div class="flex flex-col relative">
		<LandingScreen v-if="modalType == 'LANDING_SCREEN'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10"></LandingScreen>
		<RegionModalFreljordModal v-if="modalType == 'FRELJORD'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10 min-h-fit"></RegionModalFreljordModal>
		<RegionModalNoxusModal v-if="modalType == 'NOXUS'" @close_modal="closeModal"
		class="absolute top-0 left-0 w-full h-full z-10 min-h-fit"></RegionModalNoxusModal>
		<RegionModalIoniaModel v-if="modalType == 'IONIA'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10 min-h-fit"></RegionModalIoniaModel>
		<RegionModalBilgewaterModal v-if="modalType == 'BILGEWATER'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10 min-h-fit"></RegionModalBilgewaterModal>
		<RegionModalShadowIslesModal v-if="modalType == 'SHADOW_ISLES'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10 min-h-fit"></RegionModalShadowIslesModal>
		<RegionModalIxtalModal v-if="modalType == 'IXTAL'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10 min-h-fit"></RegionModalIxtalModal>
		<RegionModalShurimaModal v-if="modalType == 'SHURIMA'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10 min-h-fit"></RegionModalShurimaModal>
		<RegionModalTargonModal v-if="modalType == 'TARGON'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10 min-h-fit"></RegionModalTargonModal>
		<RegionModalDemaciaModal v-if="modalType == 'DEMACIA'" @close_modal="closeModal" class="absolute top-0 left-0 w-full h-full z-10 min-h-fit"></RegionModalDemaciaModal>
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
