<template>
	<div style="width: 400px"><canvas ref="radarContainer" class="border-ionia-primary border-2 bg-ionia-secondary"></canvas></div>
</template>

<script setup lang="ts">
const chartContainer = useTemplateRef("radarContainer")
import { Chart, RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend } from "chart.js/auto"

const props = defineProps({
	combat: {
		type: Number,
		required: false,
		default: 0,
	},
	teamContribution: {
		type: Number,
		required: false,
		default: 0,
	},
	visionAndAwareness: {
		type: Number,
		required: false,
		default: 0,
	},
	resourceEfficiency: {
		type: Number,
		required: false,
		default: 0,
	},
	consistency: {
		type: Number,
		required: false,
		default: 0,
	},
})

onMounted(() => {
	const chart = new Chart(chartContainer.value!, {
		type: "radar",
		data: {
			labels: ["Combat", "Team Contribution", "Vision and Awareness", "Resource Efficiency", "Consistency"],
			datasets: [
				{
					label: "Player Performance",
					data: [props.combat, props.teamContribution, props.visionAndAwareness, props.resourceEfficiency, props.consistency],
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
						stepSize: 1,
						color: "#FFF",
						backdropColor: "rgba(0,0,0,0)",
					},
					grid: {
						color: "rgba(200,200,200,0.2)",
					},
					angleLines: {
						color: "rgba(200,200,200,0.2)",
					},
					pointLabels: {
						color: "#FFF",
						font: {
							size: 12,
						},
					},
				},
			},
			plugins: {
				legend: {
					display: true,
					position: "bottom",
                    labels: {
                        color: "#FFF",
                    },
				},
			},
		},
	})
})
</script>
