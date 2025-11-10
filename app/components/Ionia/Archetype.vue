<template>
	<div :class="[bgColor]">
		<div :class="['flex-row', bgColor, 'justify-center']">
			<div :class="['w-full', 'flex', 'flex-col', 'text-center', 'bg-black', 'border-2', borderColor, 'text-white', 'items-center', 'p-10', 'mb-18']">
				<p class="text-5xl pb-10">{{ titleText }}</p>
				<p>{{ profileText }}</p>
			</div>

			<p :class="['w-full', 'text-center', 'bg-black', 'border-2', borderColor, 'text-white', 'items-center', 'p-10', 'mb-18']">{{ descriptionText }}</p>

			<!-- <div class="flex justify-center mb-10">
			<img :src="`/lane-icons/${playerArchetype}_icon.png`" class="w-12 h-12 object-contain" />
		    </div> -->
		</div>
		<hr :class="['border', borderColor, 'my-4']" />
	</div>
	<div>
		<p class="p-10 text-white text-3xl text-cinzel">BALANCE OF STRENGTHS</p>
	</div>
</template>

<script setup lang="ts">
defineProps({
	bgColor: String,
	borderColor: String,
	sectionText: String,
	titleText: String,
	icon: String,
	profileText: String,
	descriptionText: String,
})
</script>
