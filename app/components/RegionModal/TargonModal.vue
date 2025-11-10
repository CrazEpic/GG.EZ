<template>
	<div class="flex absolute top-0 left-0 w-full h-full bg-targon-secondary font-cinzel text-center">
		<!-- <RegionOverlayTitle v-bind="targonData" /> -->
		<ChampionConstellation
			:champion="mainChampion"
			class="grow"
			@change_drawer="
				async (drawer, resetCameraCallback, focusOnCallback, x, y) => {
					if (drawerType == drawer) {
						drawerType = 'None'
						await resetCameraCallback()
					} else {
						drawerType = drawer
						await focusOnCallback(x, y)
					}
				}
			"
		></ChampionConstellation>
		<!-- <Continue class="absolute top-0.5 bottom-20" v-bind="targonContinue" @close_modal="$emit('close_modal')" /> -->
		<ConstellationDrawerAbilityDrawer
			v-if="drawerType == 'ABILITY'"
			class="absolute right-0 top-0 w-90 h-full border-2 border-black bg-targon-secondary"
		></ConstellationDrawerAbilityDrawer>
		<ConstellationDrawerPlaytimeDrawer
			v-if="drawerType == 'PLAYTIME'"
			class="absolute right-0 top-0 w-90 h-full border-2 border-black bg-targon-secondary"
		></ConstellationDrawerPlaytimeDrawer>
		<ConstellationDrawerBuildDrawer
			v-if="drawerType == 'BUILD'"
			class="absolute right-0 top-0 w-90 h-full border-2 border-black bg-targon-secondary"
		></ConstellationDrawerBuildDrawer>
		<ConstellationDrawerGoldGeneratingDrawer
			v-if="drawerType == 'GOLDGENERATING'"
			class="absolute right-0 top-0 w-90 h-full border-2 border-black bg-targon-secondary"
		></ConstellationDrawerGoldGeneratingDrawer>
		<ConstellationDrawerKDADrawer
			v-if="drawerType == 'KDADRAWER'"
			class="absolute right-0 top-0 w-90 h-full border-2 border-black bg-targon-secondary"
		></ConstellationDrawerKDADrawer>
		<ConstellationDrawerMultikillsDrawer
			v-if="drawerType == 'MULTIKILLS'"
			class="absolute right-0 top-0 w-90 h-full border-2 border-black bg-targon-secondary"
		></ConstellationDrawerMultikillsDrawer>
		<ConstellationDrawerSuperlativesDrawer
			v-if="drawerType == 'SUPERLATIVES'"
			class="absolute right-0 top-0 w-90 h-full border-2 border-black bg-targon-secondary"
		></ConstellationDrawerSuperlativesDrawer>
		<button
			:class="`absolute left-1/2 bottom-2 -translate-x-1/2 bg-black border-2 px-10 py-1 w-64 h-16 ${targonContinue.bgColor} text-white cursor-pointer mb-20`"
			@click="$emit('close_modal')"
		>
			{{ targonContinue.continueText }}
		</button>
	</div>
</template>

<script setup lang="ts">
const playerDataStore = usePlayerDataStore()
const mainChampion = playerDataStore.playerData?.sr.targon_info.most_played_champion?.[0]
const drawerType = ref("None")

const targonData = {
	backdropImage: "/region-backdrop/targonbackdrop.png",
	title: "Targon",
	bgColor: "bg-targon-secondary",
	borderColor: "border-targon-primary",
}

const targonContinue = {
	bgColor: "bg-targon-secondary",
	borderColor: "border-targon-primary",
	continueText: "Continue Your Journey",
}

const audio = ref()

onMounted(() => {
    audio.value = new Audio("soundfiles/region_music/targon.mp3")
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
