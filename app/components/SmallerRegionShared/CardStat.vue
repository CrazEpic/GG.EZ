<template>
	<div :class="['h-full', 'w-70', 'flex', 'flex-col', 'items-center', 'text-white', borderColor, 'border-2']">
		<p :class="['text-white', 'text-lg', 'pt-5']">{{ title }}</p>

		<div v-if="isGraphCard">
			<div class="w-full" flex justify-center><canvas ref="pieContainer" class="max-w-[full] max-h-[full]"></canvas></div>
		</div>
		<!-- else if -->
		<div v-else>
			<div class="flex-col py-20">
				<div v-for="(val, key) in typeof values === 'object' && values !== null ? values : {}">{{ key }}: {{ val }}</div>
			</div>

			<div v-if="typeof values !== 'object' || values === null" class="text-sm">
				{{ values }}
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import Chart from "chart.js/auto"

const props = defineProps({
	borderColor: String,
	title: String,
	values: [Object, Number, String],
	showGraph: Boolean,
})

const playerDataStore = usePlayerDataStore()
const totalPhysicalTaken = playerDataStore.playerData?.sr.freljord_info.total_physical_damage_taken
const totalMagicTaken = playerDataStore.playerData?.sr.freljord_info.total_magic_damage_taken
const totalTrueTaken = playerDataStore.playerData?.sr.freljord_info.total_true_damage_taken
const isGraphCard = computed(() => props.showGraph && typeof props.values === "object")
const totalDamageTaken = (totalPhysicalTaken ?? 0) + (totalMagicTaken ?? 0) + (totalTrueTaken ?? 0)
const physicalPercentage = ((totalPhysicalTaken ?? 0) / totalDamageTaken) * 100
const magicPercentage = ((totalMagicTaken ?? 0) / totalDamageTaken) * 100
const truePercentage = ((totalTrueTaken ?? 0) / totalDamageTaken) * 100

const pieContainer = ref<HTMLCanvasElement | null>(null)
let chart: Chart | null = null

onMounted(() => {
	if (!pieContainer.value) return

	chart = new Chart(pieContainer.value, {
		type: "pie",
		data: {
			labels: ["Physical", "Magic", "True"],
			datasets: [
				{
					label: "Damage Distribution",
					data: [physicalPercentage, magicPercentage, truePercentage],
					backgroundColor: [
						"rgba(255, 0, 0, 0.4)", // physical = red
						"rgba(0, 112, 255, 0.4)", // magic = blue
						"rgba(255, 255, 255, 0.6)", // true = white
					],
				},
			],
		},
		options: {
			responsive: true,
		},
	})
})
</script>
