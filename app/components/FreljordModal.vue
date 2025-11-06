<template>
	<div class="bg-black">
		<p class="text-white">Freljord</p>
		<Carousel>
			<p>1</p>
			<p>2</p>
			<p>3</p>
			<p>4</p>
			<p>5</p>
		</Carousel>
		<button class="text-white cursor-pointer" @click="$emit('close_modal')">Get started</button>
	</div>
</template>

<script setup lang="ts">
import Carousel from "./Carousel.vue"
</script>