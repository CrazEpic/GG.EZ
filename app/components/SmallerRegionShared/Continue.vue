<template>
	<div :class="[bgColor, 'px-16']">
		<hr :class="['border', borderColor]" />
		<h1 :class="['text-white', 'm-6']">{{continueText}}</h1>
		<button :class="['bg-black', 'border-2', 'px-10', 'py-1', borderColor, 'text-white', 'cursor-pointer', 'mb-20']" @click="$emit('close_modal')">
			{{buttonText}}
		</button>
	</div>
</template>

<script setup lang="ts">
    defineProps({
        bgColor: String,
        borderColor: String,
        continueText: String,
        buttonText: String,
    })
</script>