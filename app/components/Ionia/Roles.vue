<template>
	<div :class="[bgColor]">
		<h1 :class="['text-white', 'mb-6']">{{ sectionText }}</h1>

		<div class="flex justify-center mb-10">
			<img :src="`/lane-icons/${mostPlayedLane}_icon.png`" class="w-12 h-12 object-contain" />
		</div>

		<hr :class="['border', borderColor, 'my-4']" />
	</div>
</template>

<script setup lang="ts">
defineProps({
	bgColor: String,
	borderColor: String,
	sectionText: String,
	mostPlayedLane: String,
})
</script>
