<template>
	<div :class="['h-full', 'w-70', 'flex', 'flex-col', 'items-center', 'text-white', borderColor, 'border-2']">
		<p :class="['text-white', 'text-lg', 'pt-5']">{{ title }}</p>

		<!--Graph Card-->
		<div v-if="isGraphCard">
			<div class="w-full flex justify-center py-5 card overflow-hidden">
				<canvas ref="pieContainer" class="max-w-full max-h-full"></canvas>
			</div>

			<p class="pt-3" v-for="(value, index) in graphLabels" :key="index">{{ value }}: {{ graphData[index] }}</p>
		</div>

		<div v-else-if="Array.isArray(topItems)">
			<div class="flex justify-center items-center gap-4 p-30">
				<div v-for="(item, index) in topItems" :key="index" class="flex flex-col items-center">
					<img :src="`items/${item[0]}.png`" alt="item icon" class="w-12 h-12 object-contain" />
					<span class="text-sm mt-1">{{ item[1] }} purchases</span>
				</div>
			</div>
		</div>

		<!-- Items Card -->
		<div v-else>
			<div class="flex-col text-lg py-20">
				<div class="py-5" v-for="(val, key) in typeof value === 'object' && value !== null ? value : {}">{{ key }}: {{ val }}</div>
			</div>

			<div v-if="typeof value !== 'object' || value === null" class="text-3xl">
				{{ value }}
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import Chart from "chart.js/auto"
import { Comment } from "vue"

const props = defineProps({
	borderColor: String,
	title: String,
	value: [Object, Number, String],
	showGraph: Boolean,
	graphType: String,
	graphData: Array,
	graphLabels: Array,
	graphColors: Array,
	topItems: Array,
})

const isGraphCard = computed(() => props.showGraph && Array.isArray(props.graphData))

const pieContainer = ref<HTMLCanvasElement | null>(null)
let chart: Chart | null = null

onMounted(() => {
	if (!pieContainer.value) return

	chart = new Chart(pieContainer.value, {
		type: props.graphType,
		data: {
			labels: props.graphLabels,
			datasets: [
				{
					label: props.graphLabels,
					data: props.graphData,
					backgroundColor: props.graphColors,
				},
			],
		},
		options: {
			responsive: true,
			indexAxis: props.graphType === "bar" ? "y" : "x",
			scales:
				props.graphType === "bar"
					? {
							x: { beginAtZero: true, ticks: { display: false } },
						}
					: {},
			plugins: {
				legend: {
					display: props.graphType !== "bar",
				},
				tooltip: {
					enabled: false, // removes hover stats
				},
			},
		},
	})
})
</script>
