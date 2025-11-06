<template>
	<div class="w-full h-full bg-freljord-secondary font-cinzel text-center">
		<div class="w-full h-48 overflow-hidden brightness-70">
			<img src="/region-backdrop/freljordbackdrop.jpg" />
		</div>
		<div class="px-16 bg-freljord-secondary">
			<div>
				<p class="text-white text-4xl mt-8">The Freljord</p>
				<p class="text-white text-md mb-2">Survival Through Unity and Strength</p>
				<hr class="border border-freljord-primary mb-8" />
			</div>
			<p class="text-white text-md">PICK A CARD TO COLLECT</p>
			<Carousel class="my-8">
				<p class="h-full flex items-center justify-center text-white border-freljord-primary border-2">damageTaken → Total (physical, magic, true)</p>
				<p class="h-full flex items-center justify-center text-white border-freljord-primary border-2">% of Team Damage Soaked → Average</p>
				<p class="h-full flex items-center justify-center text-white border-freljord-primary border-2">totalHeal → Total, totalHealsOnTeammates → Total</p>
				<p class="h-full flex items-center justify-center text-white border-freljord-primary border-2">avg survivalRatio</p>
				<p class="h-full flex items-center justify-center text-white border-freljord-primary border-2">max timePlayed</p>
			</Carousel>
			<div>
				<hr class="border border-freljord-primary m-4" />
				<h1 class="text-white mb-16">Your Achievements</h1>
				<div class="flex justify-center">
					<p class="w-140 text-center bg-black border-2 border-freljord-primary text-white items-center p-10 mb-10">
						Your longest game was on 11/2/2025, lasting 100 minutes. And yada YADA YADA
					</p>
				</div>
			</div>
			<hr class="border border-freljord-primary mt-10" />
			<div>
				<h1 class="text-white m-6">YOU ENDURED THE FROST</h1>
				<button class="bg-black border-2 px-10 py-1 border-freljord-primary text-white cursor-pointer" @click="$emit('close_modal')">
					Continue Your Journey
				</button>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
	import RegionOverlayTitle from './RegionOverlayTitle.vue';

	const freljordData = {
		backdropImage: '/region-backdrop/freljordbackdrop.jpg',
		title: 'The Freljord',
        description: 'Survival Through Unity and Strength',
        bgColor: 'bg-freljord-secondary',
        borderColor: 'bg-freljord-primary'
	}
	// network fetching
</script>
