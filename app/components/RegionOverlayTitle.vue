<template>
	<div class="w-full h-48 overflow-hidden brightness-70">
		<img :src="backdropImage" />
	</div>
	<div :class="['px-16', bgColor]">
		<p class="text-white text-4xl mt-8">{{ title }}</p>
		<p class="text-white text-md mb-2">{{ description }}</p>
		<hr :class="['border', borderColor, 'mb-8']" />
	</div>
</template>

<script setup lang="ts">
defineProps({
	backdropImage: String,
	title: String,
	description: String,
	bgColor: String,
	borderColor: String,
})
</script>