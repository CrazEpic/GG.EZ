<template>
	<div class="w-full h-full bg-freljord-secondary font-cinzel text-center">
		<div style="width: 800px"><canvas ref="radarContainer"></canvas></div>
		<Continue v-bind="freljordContinue" @close_modal="$emit('close_modal')" />
	</div>
</template>

<script setup lang="ts">
const chartContainer = useTemplateRef("radarContainer")
import { Chart, RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend } from "chart.js/auto"

const freljordContinue = {
	bgColor: "bg-freljord-secondary",
	borderColor: "border-freljord-primary",
	continueText: "YOU ENDURED THE FROST",
	buttonText: "Continue Your Journey",
}

onMounted(() => {
	const chart = new Chart(chartContainer.value!, {
		type: "radar",
		data: {
			labels: ["Combat", "Map Influence", "Objective Participation", "Vision and Awareness", "Resource Efficiency", "Consistency"],
			datasets: [
				{
					label: "Player Performance",
					data: [0.8, 0.6, 0.75, 0.9, 0.7, 0.85],
					fill: true,
					backgroundColor: "rgba(54, 162, 235, 0.2)",
					borderColor: "rgba(54, 162, 235, 1)",
					pointBackgroundColor: "rgba(54, 162, 235, 1)",
					pointBorderColor: "#fff",
					pointHoverBackgroundColor: "#fff",
					pointHoverBorderColor: "rgba(54, 162, 235, 1)",
				},
			],
		},
		options: {
			scales: {
				r: {
					min: 0,
					max: 1,
					ticks: {
						stepSize: 0.2,
						color: "#999",
					},
					grid: {
						color: "rgba(200,200,200,0.2)",
					},
					angleLines: {
						color: "rgba(200,200,200,0.2)",
					},
					pointLabels: {
						color: "#333",
						font: {
							size: 12,
						},
					},
				},
			},
			plugins: {
				legend: {
					display: true,
					position: "top",
				},
			},
		},
	})
})
</script>
