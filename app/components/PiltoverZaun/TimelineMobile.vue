<template>
	<div class="w-full">
		<div class="flex flex-col justify-center items-center text-center text-sm text-white mt-2 space-y-2">
			<div class="w-full"><img src="/welcome_to_noxus.png" /></div>
			<div>
				<div class="w-full truncate"><p>Season 1</p></div>

				<div class="w-full truncate"><p>Welcome to Noxus</p></div>
			</div>
			<div class="w-full">
				<button
					@click="$emit('selectedNote', note1)"
					:class="`p-2 truncate border-2 cursor-pointer bg-${props.region == 'PILTOVER' ? 'piltover' : 'zaun'}-secondary border-${props.region == 'PILTOVER' ? 'piltover' : 'zaun'}-primary`"
				>
					{{ note1 }}
				</button>
			</div>
		</div>

		<div class="flex flex-col justify-center items-center text-center text-sm text-white mt-2 space-y-2">
			<div class="w-full"><img src="/spirit_blossom.png" /></div>
			<div>
				<div class="w-full truncate"><p>Season 2</p></div>

				<div class="w-full truncate"><p>Spirit Blossom Beyond</p></div>
			</div>
			<div class="w-full">
				<button
					@click="$emit('selectedNote', note2)"
					:class="`p-2 truncate border-2 cursor-pointer bg-${props.region == 'PILTOVER' ? 'piltover' : 'zaun'}-secondary border-${props.region == 'PILTOVER' ? 'piltover' : 'zaun'}-primary`"
				>
					{{ note2 }}
				</button>
			</div>
		</div>

		<div class="flex flex-col justify-center items-center text-center text-sm text-white mt-2 space-y-2">
			<div class="w-full"><img src="/trials_of_twilight.png" /></div>
			<div>
				<div class="w-full truncate"><p>Season 3</p></div>

				<div class="w-full truncate"><p>Trials of Twilight</p></div>
			</div>
			<div class="w-full">
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
