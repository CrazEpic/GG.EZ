<template>
	<div class="w-full h-full bg-ionia-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="ioniaData" />
		<div class="px-4 sm:px-16">
			<div class="flex flex-wrap justify-evenly">
				<div class="w-fit">
					<IoniaRadarChart
						ref="playerRadarChart"
						:combat="playerDataStore.playerData?.sr.ionia_info.combat_effectiveness ?? 0"
						:team-contribution="playerDataStore.playerData?.sr.ionia_info.team_contribution ?? 0"
						:visionAndAwareness="playerDataStore.playerData?.sr.ionia_info.vision_awareness ?? 0"
						:resourceEfficiency="playerDataStore.playerData?.sr.ionia_info.resource_efficiency ?? 0"
						:consistency="playerDataStore.playerData?.sr.ionia_info.consistency ?? 0"
					/>
					<p class="text-white">Craz</p>
				</div>
				<div v-if="selectedPro != ''" class="w-fit">
					<IoniaRadarChart :combat="0.5" :team-contribution="0.6" :visionAndAwareness="0.75" :resourceEfficiency="0.9" :consistency="0.7" />
					<p class="text-white">{{ selectedPro }}</p>
				</div>
			</div>
			<IoniaProsDisplay
				@choose_pro="
					(pro) => {
						selectedPro = pro
						scrollPlayerRadarToTop()
					}
				"
				:pro_1="pros[0].name"
				:pro_1_img="pros[0].img"
				:pro_2="pros[1].name"
				:pro_2_img="pros[1].img"
				:pro_3="pros[2].name"
				:pro_3_img="pros[2].img"
			></IoniaProsDisplay>
			<SmallerRegionSharedContinue v-bind="ioniaContinue" @close_modal="$emit('close_modal')" />
		</div>
	</div>
</template>

<script setup lang="ts">
const playerRadarChart = useTemplateRef("playerRadarChart")
const playerDataStore = usePlayerDataStore()

const pros = [
	{ name: "Dan", img: "dan_the_penguin.png" },
	{ name: "James", img: "dan_the_penguin.png" },
	{ name: "Lucy", img: "dan_the_penguin.png" },
]

const selectedPro = ref("")

const ioniaData = {
	backdropImage: "/region-backdrop/ioniabackdrop.png",
	title: "The ionia",
	description: "Survival Through Unity and Strength",
	bgColor: "bg-ionia-secondary",
	borderColor: "border-ionia-primary",
}

const ioniaContinue = {
	bgColor: "bg-ionia-secondary",
	borderColor: "border-ionia-primary",
	continueText: "YOU ENDURED THE FROST",
	buttonText: "Continue Your Journey",
}

const scrollPlayerRadarToTop = () => {
	const radarElement = playerRadarChart.value?.$el as HTMLElement
	if (radarElement) {
		radarElement.scrollIntoView({ behavior: "smooth", block: "start" })
	}
}
</script>
