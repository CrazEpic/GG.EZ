<template>
	<div class="w-full h-full bg-demacia-secondary font-cinzel text-center">
		<SmallerRegionSharedRegionOverlayTitle v-bind="demaciaData" />

		<div class="px-4 sm:px-16">
			<!-- <DemaciaPostcard></DemaciaPostcard> -->
			<h2 class="text-lg font-bold mb-4 text-white">Most Common Teammates</h2>
			<table class="min-w-full border border-demacia-primary">
				<thead>
					<tr class="bg-default-secondary text-center justify-between">
						<th class="px-4 py-2 text-white">Player</th>
						<th class="px-4 py-2 text-white">Matches</th>
						<th class="px-4 py-2 text-white">Winrate</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="teammate in demaciaInfo.most_common_teammates" :key="teammate.puuid" class="border-t">
						<td class="px-4 py-2 text-white">{{ teammate.riotIdGameName }}#{{ teammate.riotIdTagline }}</td>
						<td class="px-4 py-2 text-white">{{ teammate.matches }}</td>
						<td class="px-4 py-2 text-white">{{ calculateWinrate(teammate) }}%</td>
					</tr>
				</tbody>
			</table>
		</div>

		<div class="w-full bg-default-secondary p-6 text-white">
			<h2 class="text-2xl font-bold text-center mb-4">Career Highlights</h2>

			<div class="grid grid-cols-2 md:grid-cols-3 gap-4 text-center">
				<!-- Matches SR -->
				<div class="bg-demacia-primary p-4 text-white">
					<div class="text-xl font-semibold">{{ usePlayerDataStore().playerData?.overview.matches_counted_sr }}</div>
					<div class="text-sm uppercase">Matches SR</div>
				</div>

				<!-- Matches ARAM -->
				<div class="bg-demacia-primary p-4 text-white">
					<div class="text-xl font-semibold">{{ usePlayerDataStore().playerData?.overview.matches_counted_aram }}</div>
					<div class="text-sm uppercase">Matches ARAM</div>
				</div>

				<!-- Play Time SR -->
				<div class="bg-demacia-primary p-4 text-white">
					<div class="text-xl font-semibold">{{ formatTime(usePlayerDataStore().playerData?.overview.play_time_sr) }}</div>
					<div class="text-sm uppercase">Play Time SR</div>
				</div>

				<!-- Play Time ARAM -->
				<div class="bg-demacia-primary p-4 text-white">
					<div class="text-xl font-semibold">{{ formatTime(usePlayerDataStore().playerData?.overview.play_time_aram) }}</div>
					<div class="text-sm uppercase">Play Time ARAM</div>
				</div>

				<!-- Wins SR -->
				<div class="bg-demacia-primary p-4 text-white">
					<div class="text-xl font-semibold">{{ usePlayerDataStore().playerData?.overview.wins_sr }}</div>
					<div class="text-sm uppercase">Wins SR</div>
				</div>

				<!-- Wins ARAM -->
				<div class="bg-demacia-primary p-4 text-white">
					<div class="text-xl font-semibold">{{ usePlayerDataStore().playerData?.overview.wins_aram }}</div>
					<div class="text-sm uppercase">Wins ARAM</div>
				</div>
			</div>
		</div>
		<SmallerRegionSharedContinue v-bind="demaciaContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">
const demaciaInfo = ref({
	most_common_teammates: useSessionStore().displaySR
		? usePlayerDataStore().playerData?.sr.demacia_info.most_common_teammates.map((teammate) => ({
				puuid: teammate.puuid,
				riotIdGameName: teammate.riotIdGameName,
				riotIdTagline: teammate.riotIdTagline,
				matches: teammate.matches,
				wins: teammate.wins,
			}))
		: usePlayerDataStore().playerData?.aram.demacia_info.most_common_teammates.map((teammate) => ({
				puuid: teammate.puuid,
				riotIdGameName: teammate.riotIdGameName,
				riotIdTagline: teammate.riotIdTagline,
				matches: teammate.matches,
				wins: teammate.wins,
			})),
})

const calculateWinrate = (teammate) => {
	if (teammate.matches === 0) return 0
	return ((teammate.wins / teammate.matches) * 100).toFixed(1)
}
// Optional helper function to format play time
function formatTime(minutes) {
	const hrs = Math.floor(minutes / 60)
	const mins = Math.trunc(minutes % 60) // truncate decimal part
	return `${hrs}h ${mins}m`
}

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
	continueText: "YOU'VE PROVEN YOUR HONOR",
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
