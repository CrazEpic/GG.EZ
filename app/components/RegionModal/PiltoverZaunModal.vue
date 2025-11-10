<template>
	<div :class="`w-full h-full font-cinzel text-center ${currentRegion == 'PILTOVER' ? 'bg-piltover-secondary' : 'bg-zaun-secondary'}`">
		<div v-if="currentRegion == 'PILTOVER'">
			<SmallerRegionSharedRegionOverlayTitle v-bind="piltoverData" />
			<div class="px-4 sm:px-16">
				<div class="flex justify-between">
					<button class="bg-black w-16 h-16 sticky top-0 cursor-pointer" @click="((currentRegion = 'PILTOVER'), (selectedNote = ''))"></button>
					<button
						class="bg-black w-16 h-16 sticky top-0 cursor-pointer"
						@click="
							() => {
								currentRegion = 'ZAUN'
								selectedNote = ''
								playChemtech()
							}
						"
					></button>
				</div>

				<PiltoverZaunTimelineMobile
					v-if="windowWidth < 640"
					note1="Observation #1"
					note2="Observation #2"
					note3="Observation #3"
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
					note1="Observation #1"
					note2="Observation #2"
					note3="Observation #3"
					region="PILTOVER"
					@selectedNote="
						(note) => {
							selectedNote = note
						}
					"
				/>
				<div ref="piltoverNoteContent" class="bg-piltover-secondary border-piltover-primary border-2 p-2">
					<p v-if="selectedNote" class="text-white">
						{{ selectedNote }} Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat.
						In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus
						bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad
						litora torquent per conubia nostra inceptos himenaeos.
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
					<button
						class="bg-black w-16 h-16 sticky top-0 cursor-pointer"
						@click="
							() => {
								currentRegion = 'PILTOVER'
								selectedNote = ''
								playHextech()
							}
						"
					></button>
					<button class="bg-black w-16 h-16 sticky top-0 cursor-pointer" @click="((currentRegion = 'ZAUN'), (selectedNote = ''))"></button>
				</div>
				<PiltoverZaunTimelineMobile
					v-if="windowWidth < 640"
					note1="Observation #1"
					note2="Observation #2"
					note3="Observation #3"
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
					note1="Observation #1"
					note2="Observation #2"
					note3="Observation #3"
					region="ZAUN"
					@selectedNote="
						(note) => {
							selectedNote = note
						}
					"
				/>
				<div ref="zaunNoteContent" class="bg-zaun-secondary border-zaun-primary border-2 p-2">
					<p v-if="selectedNote" class="text-white">
						{{ selectedNote }} Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat.
						In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus
						bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad
						litora torquent per conubia nostra inceptos himenaeos.
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

const piltoverData = {
	backdropImage: "/region-backdrop/piltoverbackdrop.png",
	title: "Piltover",
	description: "REPLACE ME",
	bgColor: "bg-piltover-secondary",
	borderColor: "border-piltover-primary",
}

const piltoverContinue = {
	bgColor: "bg-piltover-secondary",
	borderColor: "border-piltover-primary",
	continueText: "YOU'VE ENDURED THE FROST",
	buttonText: "Continue Your Journey",
}

const zaunData = {
	backdropImage: "/region-backdrop/zaunbackdrop.png",
	title: "Zaun",
	description: "REPLACE ME",
	bgColor: "bg-zaun-secondary",
	borderColor: "border-zaun-primary",
}

const zaunContinue = {
	bgColor: "bg-zaun-secondary",
	borderColor: "border-zaun-primary",
	continueText: "YOU'VE ENDURED THE FROST",
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
const hextechSfx = ref<null | HTMLAudioElement>(null)
const chemtechSfx = ref<null | HTMLAudioElement>(null)

const playHextech = () => {
	if (hextechSfx.value) {
		hextechSfx.value.currentTime = 0
		hextechSfx.value.play()
	}
}

const playChemtech = () => {
	if (chemtechSfx.value) {
		chemtechSfx.value.currentTime = 0
		chemtechSfx.value.play()
	}
}

onMounted(() => {
	audio.value = new Audio("soundfiles/region_music/piltover.mp3")
	audio.value.loop = true
	audio.value.volume = 0.5
	audio.value.play()

	hextechSfx.value = new Audio("soundfiles/sfx/hextech.mp3")
	chemtechSfx.value = new Audio("soundfiles/sfx/chemtech.mp3")
})

onBeforeUnmount(() => {
	if (audio.value) {
		audio.value.pause()
		audio.value.currentTime = 0
	}
})
</script>
