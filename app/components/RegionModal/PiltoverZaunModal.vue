<template>
	<div :class="`w-full h-full font-cinzel text-center ${currentRegion == 'PILTOVER' ? 'bg-piltover-secondary' : 'bg-zaun-secondary'}`">
		<div v-if="currentRegion == 'PILTOVER'">
			<SmallerRegionSharedRegionOverlayTitle v-bind="piltoverData" />
			<div class="px-4 sm:px-16">
				<div class="flex justify-between">
					<button class="bg-black w-16 h-16 sticky top-0 cursor-pointer" @click="((currentRegion = 'PILTOVER'), (selectedNote = ''))"></button>
					<button class="bg-black w-16 h-16 sticky top-0 cursor-pointer" @click="((currentRegion = 'ZAUN'), (selectedNote = ''))"></button>
				</div>

				<PiltoverZaunTimelineMobile
					v-if="windowWidth < 640"
					note1="Piltover Observation #1"
					note2="Piltover Observation #2"
					note3="Piltover Observation #3"
					region="PILTOVER"
					@selectedNote="
						(note) => {
							selectedNote = note
							scrollIntoPiltoverNote()
						}
					"
				></PiltoverZaunTimelineMobile>
				<PiltoverZaunTimeline
					v-else
					note1="Piltover Observation #1"
					note2="Piltover Observation #2"
					note3="Piltover Observation #3"
					region="PILTOVER"
					@selectedNote="
						(note) => {
							selectedNote = note
						}
					"
				/>
				<div ref="piltoverNoteContent" class="bg-piltover-secondary border-piltover-primary border-2 p-2">
					<p v-if="selectedNote" class="text-white">
						{{ computedPlayerData(selectedNote) }}
					</p>
					<p v-else class="text-white">{{ defaultNoteContent }}</p>
				</div>
				<SmallerRegionSharedContinue v-bind="piltoverContinue" @close_modal="$emit('close_modal')" />
			</div>
		</div>
		<div v-else-if="currentRegion == 'ZAUN'">
			<SmallerRegionSharedRegionOverlayTitle v-bind="zaunData" />

			<div class="px-4 sm:px-16">
				<div class="flex justify-between">
					<button class="bg-black w-16 h-16 sticky top-0 cursor-pointer" @click="((currentRegion = 'PILTOVER'), (selectedNote = ''))"></button>
					<button class="bg-black w-16 h-16 sticky top-0 cursor-pointer" @click="((currentRegion = 'ZAUN'), (selectedNote = ''))"></button>
				</div>
				<PiltoverZaunTimelineMobile
					v-if="windowWidth < 640"
					note1="Zaun Observation #1"
					note2="Zaun Observation #2"
					note3="Zaun Observation #3"
					region="ZAUN"
					@selectedNote="
						(note) => {
							selectedNote = note
							scrollIntoZaunNote()
						}
					"
				></PiltoverZaunTimelineMobile>
				<PiltoverZaunTimeline
					v-else
					note1="Zaun Observation #1"
					note2="Zaun Observation #2"
					note3="Zaun Observation #3"
					region="ZAUN"
					@selectedNote="
						(note) => {
							selectedNote = note
						}
					"
				/>
				<div ref="zaunNoteContent" class="bg-zaun-secondary border-zaun-primary border-2 p-2">
					<p v-if="selectedNote" class="text-white">
						{{ computedPlayerData(selectedNote) }}
					</p>
					<p v-else class="text-white">{{ defaultNoteContent }}</p>
				</div>
				<SmallerRegionSharedContinue v-bind="zaunContinue" @close_modal="$emit('close_modal')" />
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
const currentRegion = ref<"PILTOVER" | "ZAUN">("PILTOVER")
const playerDataStore = usePlayerDataStore()
const piltoverNoteContent = useTemplateRef("piltoverNoteContent")
const zaunNoteContent = useTemplateRef("zaunNoteContent")

const defaultNoteContent = "Select an observation to see more details here."

const scrollIntoPiltoverNote = () => {
	piltoverNoteContent.value?.scrollIntoView({ behavior: "smooth", block: "start" })
}

const scrollIntoZaunNote = () => {
	zaunNoteContent.value?.scrollIntoView({ behavior: "smooth", block: "start" })
}

const selectedNote = ref("")

const computedPlayerData = (selected) => {
	if (selected === "Piltover Observation #1") {
		return useSessionStore().displaySR ? playerDataStore.playerData?.llm_responses.sr.piltover_response[0] : playerDataStore.playerData?.llm_responses.lr.piltover_response[0]
	} else if (selected === "Piltover Observation #2") {
		return useSessionStore().displaySR ? playerDataStore.playerData?.llm_responses.sr.piltover_response[1] : playerDataStore.playerData?.llm_responses.lr.piltover_response[1]
	} else if (selected === "Piltover Observation #3") {
		return useSessionStore().displaySR ? playerDataStore.playerData?.llm_responses.sr.piltover_response[2] : playerDataStore.playerData?.llm_responses.lr.piltover_response[2]
	} else if (selected === "Zaun Observation #1") {
		return useSessionStore().displaySR ? playerDataStore.playerData?.llm_responses.sr.zaun_response[0] : playerDataStore.playerData?.llm_responses.lr.zaun_response[0]
	} else if (selected === "Zaun Observation #2") {
		return useSessionStore().displaySR ? playerDataStore.playerData?.llm_responses.sr.zaun_response[1] : playerDataStore.playerData?.llm_responses.lr.zaun_response[1]
	} else if (selected === "Zaun Observation #3") {
		return useSessionStore().displaySR ? playerDataStore.playerData?.llm_responses.sr.zaun_response[2] : playerDataStore.playerData?.llm_responses.lr.zaun_response[2]
	} else {
		return defaultNoteContent
	}
}

const piltoverData = {
	backdropImage: "/region-backdrop/piltoverbackdrop.png",
	title: "Piltover",
	description: "The City of Progress",
	bgColor: "bg-piltover-secondary",
	borderColor: "border-piltover-primary",
}

const piltoverContinue = {
	bgColor: "bg-piltover-secondary",
	borderColor: "border-piltover-primary",
	continueText: "YOU'VE EMBRACED THE PROGRESS",
	buttonText: "Continue Your Journey",
}

const zaunData = {
	backdropImage: "/region-backdrop/zaunbackdrop.png",
	title: "Zaun",
	description: "The Undercity of Progress",
	bgColor: "bg-zaun-secondary",
	borderColor: "border-zaun-primary",
}

const zaunContinue = {
	bgColor: "bg-zaun-secondary",
	borderColor: "border-zaun-primary",
	continueText: "YOU'VE EMBRACED THE CHAOS",
	buttonText: "Continue Your Journey",
}

const windowWidth = ref(window.innerWidth)

const updateWindowWidth = () => {
	windowWidth.value = window.innerWidth
}

onMounted(() => {
	window.addEventListener("resize", updateWindowWidth)
})

onBeforeUnmount(() => {
	window.removeEventListener("resize", updateWindowWidth)
})
const audio = ref()

onMounted(() => {
	audio.value = new Audio("soundfiles/region_music/piltover.mp3")
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
