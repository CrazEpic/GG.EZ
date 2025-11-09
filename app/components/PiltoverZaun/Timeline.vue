<template>
	<div class="w-full">
		<div class="flex justify-between items-center text-center text-sm text-white mt-2">
			<div class="w-1/3"><img src="/welcome_to_noxus.png" /></div>
			<div class="w-1/3"><img src="/spirit_blossom.png" /></div>
			<div class="w-1/3"><img src="/trials_of_twilight.png" /></div>
		</div>
		<!-- Labels -->
		<div class="flex justify-between items-center text-center text-sm text-white mt-2">
			<div class="w-1/3 truncate"><p>Season 1</p></div>
			<div class="w-1/3 truncate"><p>Season 2</p></div>
			<div class="w-1/3 truncate"><p>Season 3</p></div>
		</div>
		<div class="relative w-full h-1">
			<!-- white bar -->
			<div class="absolute inset-0 bg-white"></div>

			<!-- separators -->
			<div class="absolute top-1/2 w-[4px] bg-white -translate-x-1/2 -translate-y-1/2 h-12" :style="{ left: '33.3333%' }"></div>
			<div class="absolute top-1/2 w-[4px] bg-white -translate-x-1/2 -translate-y-1/2 h-12" :style="{ left: '66.6666%' }"></div>
		</div>
		<div class="flex justify-between items-center text-center text-sm text-white mt-2">
			<div class="w-1/3 truncate"><p>Welcome to Noxus</p></div>
			<div class="w-1/3 truncate"><p>Spirit Blossom Beyond</p></div>
			<div class="w-1/3 truncate"><p>Trials of Twilight</p></div>
		</div>
		<div class="flex justify-between items-center text-center text-sm text-white mt-2">
			<div class="w-1/3">
				<button
					@click="$emit('selectedNote', note1)"
					:class="`p-2 truncate border-2 cursor-pointer bg-${props.region == 'PILTOVER' ? 'piltover' : 'zaun'}-secondary border-${props.region == 'PILTOVER' ? 'piltover' : 'zaun'}-primary`"
				>
					{{ note1 }}
				</button>
			</div>
			<div class="w-1/3">
				<button
					@click="$emit('selectedNote', note2)"
					:class="`p-2 truncate border-2 cursor-pointer bg-${props.region == 'PILTOVER' ? 'piltover' : 'zaun'}-secondary border-${props.region == 'PILTOVER' ? 'piltover' : 'zaun'}-primary`"
				>
					{{ note2 }}
				</button>
			</div>
			<div class="w-1/3">
				<button
					@click="$emit('selectedNote', note3)"
					:class="`p-2 truncate border-2 cursor-pointer bg-${props.region == 'PILTOVER' ? 'piltover' : 'zaun'}-secondary border-${props.region == 'PILTOVER' ? 'piltover' : 'zaun'}-primary`"
				>
					{{ note3 }}
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
const props = defineProps({
	note1: { type: String, required: true },
	note2: { type: String, required: true },
	note3: { type: String, required: true },
	region: { type: String, required: true },
})

const { note1, note2, note3 } = props
</script>
