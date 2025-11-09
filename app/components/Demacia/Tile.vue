<template>
	<div
		class="w-full h-full border-2 flex items-center justify-center overflow-hidden"
		:class="[customClasses, isEmpty ? 'bg-default-secondary' : 'bg-default-secondary text-white']"
		:style="{
			gridColumn: `${gridColumnStart} / span ${colSpan || 1}`,
			gridRow: `${gridRowStart} / span ${rowSpan || 1}`,
			borderColor: '#FFFFFF',
			borderWidth: '2px',
		}"
	>
		<!-- Render content -->
		<template v-if="!isEmpty">
			<!-- Text tile -->
			<span v-if="type === 'text'" class="text-center p-2">{{ text }}</span>

			<!-- Image tile -->
			<img v-else-if="type === 'image'" :src="image" class="object-cover w-full h-full" />

			<!-- Percentage tile -->
			<div v-else-if="type === 'percentage'" class="w-full h-full flex flex-col justify-end">
				<div class="bg-default-secondary w-full h-2">
					<div class="bg-default-primary h-2" :style="{ width: `${percentage}%` }"></div>
				</div>
			</div>

			<!-- Map or custom types can go here -->
		</template>

		<!-- Empty placeholder -->
		<template v-else>
			<div class="w-3/4 h-3/4 bg-default-secondary brightness-200"></div>
		</template>
	</div>
</template>

<script setup>
const props = defineProps({
	type: String,
	text: String,
	image: String,
	percentage: Number,
	mapData: Object,
	colSpan: Number,
	rowSpan: Number,
	gridColumnStart: Number,
	gridRowStart: Number,
	customClasses: String,
})

const isEmpty = computed(() => props.type === "empty")
</script>
