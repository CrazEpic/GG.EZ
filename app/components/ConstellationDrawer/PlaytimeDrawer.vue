<template>
	<div class="flex flex-col items-center px-10 text-white text-cinzel">
		<h1 class="text-3xl py-5">THE MASTER</h1>
		<div class="relative">
			<img src="/eternals/Master.png" class="w-50 h-50" />
			<img src="/eternals/IconFrame.png" class="w-50 h-50 absolute inset-0" />
		</div>
		<p class="text-md py-5">"A thousand games, a thousand insights. True craftiness is born of experience."</p>

		<div class="flex flex-col items-center justify-center text-center">
			<div class="relative w-48 h-48">
				<canvas ref="doughnutContainer"></canvas>
				<div class="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
					<p class="text-3xl font-bold">{{ winRate }}%</p>
					<p class="text-sm text-gray-400">Winrate</p>
				</div>
			</div>

			<div class="mt-6 text-xl">
				<h2 class="text-xl my-5">
					Total Games:
					<p class="font-bold text-white">{{ gameCount }}</p>
				</h2>
				<h2 class="text-2xl my-15">
					Total Play Time:
				</h2>
                <p class="text-white">{{ formattedTime }}</p>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { Chart, DoughnutController } from "chart.js"

const playerDataStore = usePlayerDataStore()

const doughnutContainer = ref<HTMLCanvasElement | null>(null)

const playTimeDisplay = playerDataStore.playerData?.sr.targon_info.play_time
const hours = Math.floor(playTimeDisplay / 60);
const minutes = playTimeDisplay % 60;
const formattedTime = `${hours}h ${Number(minutes.toFixed(0))}m`;

const gameCount = computed(() => {
	return playerDataStore.playerData?.sr.targon_info.game_count ?? 0
})

const winRate = computed(() => {
	// Using the 'win' property you provided
	const wins = playerDataStore.playerData?.sr.targon_info.win ?? 0
	const totalGames = gameCount.value

	return Math.round((wins / totalGames) * 100)
})

const lossRate = computed(() => {
	return 100 - winRate.value
})

onMounted(() => {
	if (!doughnutContainer.value || !playerDataStore.playerData) {
		return
	}

	const doughnut = new Chart(doughnutContainer.value, {
		type: "doughnut",
		data: {
			labels: ["Win", "Loss"],
			datasets: [
				{
					data: [winRate.value, lossRate.value],
					backgroundColor: ["#4ade80", "#9ca3af"],
					borderColor: "#0a0a1a",
					borderWidth: 2,
				},
			],
		},
		options: {
			responsive: true,
			maintainAspectRatio: false,
			cutout: "80%", // thins ring
			plugins: {
				legend: {
					display: false, // removes labels
				},
				tooltip: {
					enabled: false, // removes hover stats
				},
			},
		},
	})
})
</script>
