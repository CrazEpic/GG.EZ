<template>
	<div :class="['px-16', bgColor]">
		<hr :class="['border', borderColor, 'm-4']" />
		<h1 :class="['text-white', 'mb-18']">{{sectionText}}</h1>
		<div :class="['flex', bgColor, 'justify-center']">
			<p :class="['w-140', 'text-center', 'bg-black', 'border-2', borderColor, 'text-white', 'items-center', 'p-10', 'mb-18']">{{ achievementText }}</p>
		</div>
	</div>
</template>

<script setup lang="ts">
    defineProps({
        bgColor: String,
        borderColor : String,
        sectionText : String,
        achievementText: String,
    })
</script>
