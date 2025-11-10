<template>
	<div class="flex flex-col items-center px-10 text-white text-cinzel">
		<h1 class="text-3xl py-5">THE WARRIOR</h1>
		<div class="relative">
			<img src="/eternals/Warrior.png" class="w-50 h-50" />
			<img src="/eternals/IconFrame.png" class="w-50 h-50 absolute inset-0" />
		</div>
		<p class="text-md py-8">"Persistence in battle is the mark of a warrior."</p>

		<div class="flex flex-col items-center gap-4 mt-6">
			<!-- Kills -->
			<div class="flex items-center gap-2 mt-10">
				<span class="text-xl font-semibold">Kills</span>
				<img src="/drawers-icon/kill.png" class="w-6 h-6" />
				<span class="text-lg">{{ kills }}</span>
			</div>

			<!-- Deaths -->
			<div class="flex items-center gap-2 py-10">
				<span class="text-xl font-semibold w-24 text-right">Deaths</span>
				<img src="/drawers-icon/death.png" class="w-6 h-6" />
				<span class="text-lg">{{ deaths }}</span>
			</div>

			<!-- Assists -->
			<div class="flex items-center gap-2 ">
				<span class="text-xl font-semibold w-24 text-right">Assists</span>
				<img src="/drawers-icon/assist.png" class="w-6 h-6" />
				<span class="text-lg">{{ assists }}</span>
			</div>
		</div>

		<!-- KDA -->
		<div class="pt-30">
			<h2 class="text-xl">KDA</h2>
			<p class="text-lg">{{ kda }}</p>
		</div>
	</div>
</template>

<script setup lang="ts">
import { kill } from "process"

const playerDataStore = usePlayerDataStore()
const kills = playerDataStore.playerData?.sr.targon_info.kills
const deaths = playerDataStore.playerData?.sr.targon_info.deaths
const assists = playerDataStore.playerData?.sr.targon_info.assists
const kda = Number(playerDataStore.playerData?.sr.targon_info.kda.toFixed(2))

defineProps({
	kills: Number,
	deaths: Number,
	assists: Number,
	kda: Number,
})
</script>
