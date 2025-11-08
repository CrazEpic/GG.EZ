<template>
	<div :class="['h-full', 'w-70', 'flex', 'flex-col', 'items-center', 'text-white', borderColor, 'border-2']">
		<p :class="['text-white', 'text-lg', 'pt-5']">{{ title }}</p>

		<p :class="['text-white', 'text-sm', 'p-25']">{{ value }}</p>
	</div>
</template>

<script setup lang="ts">
defineProps({
	borderColor: String,
	title: String,
	value: String,
})
</script>