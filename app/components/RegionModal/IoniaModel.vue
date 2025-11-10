<template>
	<div class="w-full h-full bg-ionia-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="ioniaData" />
		<div class="px-16">
		<IoniaRoles v-bind="ioniaRoles"/>
		<IoniaArchetype v-bind="ioniaArchetype"/>
		<div class="px-4 sm:px-16">
			<div class="flex flex-wrap justify-evenly">
				<div class="w-fit">
					<p class="text-white text-2xl">{{ archetype.name }}</p>
					<IoniaRadarChart
						ref="playerRadarChart"
						:combat="playerDataStore.playerData?.sr.ionia_info.combat_effectiveness ?? 0"
						:team-contribution="playerDataStore.playerData?.sr.ionia_info.team_contribution ?? 0"
						:visionAndAwareness="playerDataStore.playerData?.sr.ionia_info.vision_awareness ?? 0"
						:resourceEfficiency="playerDataStore.playerData?.sr.ionia_info.resource_efficiency ?? 0"
						:consistency="playerDataStore.playerData?.sr.ionia_info.consistency ?? 0"
					/>
					<p class="text-white">{{summonerName}}</p>
				</div>
				<div v-if="selectedPro != ''" class="w-fit">
					<p class="text-white text-2xl">{{ proPlayersArchetype.name }}</p>
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
				:pro_1="proPlayers[0].name"
				:pro_1_img="proPlayers[0].img"
				:pro_2="proPlayers[1].name"
				:pro_2_img="proPlayers[1].img"
				:pro_3="proPlayers[2].name"
				:pro_3_img="proPlayers[2].img"
			></IoniaProsDisplay>
			<SmallerRegionSharedContinue v-bind="ioniaContinue" @close_modal="$emit('close_modal')" />
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
const playerRadarChart = useTemplateRef("playerRadarChart")
const playerDataStore = usePlayerDataStore()
const summonerName = playerDataStore.playerData?.sr.ionia_info.summonerName
const mostPlayedLane = playerDataStore.playerData?.sr.ionia_info.most_played_lane
const archetypeId = playerDataStore.playerData?.sr.ionia_info.archetype_id
const topThreePros = playerDataStore.playerData?.sr.ionia_info.top_3_pros ?? []

const archetypes = {
	0: {
		name: 'The Vision Sentinel',
		icon: "archetypes/archetype_0.png",
		profile: "High vision awareness and team contribution, with moderate combat power and efficiency.",
		description: "Strategic and map-aware, the Vision Sentinel thrives on information control and coordinated play. They set up vision, secure objectives, and keep teammates safe with strong awareness and reliable consistency. Often the quiet playmaker behind team success."
	},
	1: {
		name: 'The Resource Commander',
		icon: "archetypes/archetype_1.png",
		profile: "Excellent combat effectiveness, resource efficiency, and consistency — a well-honed, impactful style.",
		description: "Methodical and dominant, the Resource Commander squeezes maximum value from every gold piece and cooldown. Their playstyle is defined by smart resource use and consistent high output — they know how to win fights and how to stay ahead."
	},
	2: {
		name: 'The Challenger Spirit',
		icon: "archetypes/archetype_2.png",
		profile: "Even emphasis across stats but generally lower intensity — a flexible, adaptive style.",
		description: "The Challenger Spirit experiments, learns, and adapts. They’re still refining their identity, often switching between aggression and caution. Their strength lies in adaptability and openness to improvement — a foundation for future mastery."
	},
	3: {
		name: 'The Mechanical Specialist',
		icon: "archetypes/archetype_3.png",
		profile: "High combat and efficiency scores, moderate vision and team contribution.",
		description: "Skill-driven and confident, the Mechanical Specialist relies on mechanics, timing, and precision. They excel in duels and skirmishes, often taking fights into their own hands. To reach peak performance, they focus on syncing mechanics with team strategy."
	},
	4: {
		name: 'The Field General',
		icon: "archetypes/archetype_4.png",
		profile: "Well-balanced across metrics — reliable combat, solid efficiency, and good consistency.",
		description: "The Field General is adaptable and steady, balancing aggression with control. Their strength is in maintaining stability across all areas — never flashy, but always dependable. The kind of player every team can build around."
	},
}
const archetype = archetypes[archetypeId]
const proPlayersArchetype = archetypes[archetypeId]

const selectedPro = ref("")

const proPlayers = topThreePros?.map((p) => ({
	name: p[0],
	stats: p[1],
	img: `/player-icons/${p[0]}.png`,
	archetype: p[2]
}))

const ioniaData = {
	backdropImage: "/region-backdrop/ioniabackdrop.png",
	title: "The ionia",
	description: "Survival Through Unity and Strength",
	bgColor: "bg-ionia-secondary",
	borderColor: "border-ionia-primary",
}

const ioniaArchetype = {
	bgColor: 'bg-ionia-secondary',
    borderColor : 'border-ionia-primary',
    sectionText : 'YOUR ARCHETYPE IS',
	titleText: archetype.name,
    icon: archetype.icon,
    profileText: archetype.profile,
    descriptionText: archetype.description,
}

const ioniaRoles = {
	bgColor: 'bg-ionia-secondary',
    borderColor : 'border-ionia-primary',
    sectionText : 'Your most played role this year',
	mostPlayedLane : mostPlayedLane
}

const ioniaContinue = {
	bgColor: "bg-ionia-secondary",
	borderColor: "border-ionia-primary",
	continueText: "YOU'VE HONED YOUR SPIRIT",
	buttonText: "Continue Your Journey",
}

const scrollPlayerRadarToTop = () => {
	const radarElement = playerRadarChart.value?.$el as HTMLElement
	if (radarElement) {
		radarElement.scrollIntoView({ behavior: "smooth", block: "start" })
	}
}
const audio = ref()

onMounted(() => {
    audio.value = new Audio("soundfiles/region_music/ionia.mp3")
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
