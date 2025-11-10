<template>
	<div style="background-color: rgba(0, 0, 0, 0.85)">
		<Header class="sticky top-0"></Header>
		<div class="px-4 py-16 sm:px-16 flex flex-col gap-y-4 items-center justify-center">
			<div class="p-8 border-2 border-default-primary bg-default-secondary text-center w-full">
				<h1 class="text-4xl text-white mb-4">Welcome to GG.EZ</h1>
				<p class="text-white">You played. We watched. Now let's talk about it.</p>
			</div>
			<div class="p-8 border-2 border-default-primary bg-default-secondary text-center w-full">
				<p class="text-white text-sm">
					GG.EZ isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or
					managing Riot Games properties. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc.
				</p>
			</div>
			<div class="p-8 border-2 border-default-primary bg-default-secondary text-center w-full">
				<p class="text-white text-2xl">Quick Notes for Your Demo</p>
				<p class="text-white">
					TLDR: be nice to the demo. Please either search crazepic#NA1's rewind or only search your own account and wait several minutes for the
					personalized experience to load.
				</p>
				<ul class="text-white text-sm flex flex-col items-start text-left my-4">
					Details
					<li class="text-white">- Your data is not saved between sessions.</li>
					<li class="text-white">
						- The first time a summoner is searched, their data will be fetched from scratch, which may take a few moments. Subsequent searches will
						be faster.
					</li>
					<li class="text-white">- Please avoid excessive searches. each request does more than just look up a summoner.</li>
					<li class="text-white">
						- We process only Normal & Ranked Summoner's Rift matches, as well as ARAM from January 9, 2025 - November 1, 2025.
					</li>
					<li class="text-white">- For an instant demo, you can explore CrazEpic's Story, which is already precomputed.</li>
				</ul>
			</div>
			<div class="p-4 border-2 border-default-primary bg-default-secondary flex flex-row flex-wrap items-center gap-4">
				<Listbox as="div" v-model="selectedRegion" class="relative w-28">
					<ListboxButton
						class="w-full py-2 px-2 text-white text-center bg-default-secondary hover:brightness-200 cursor-pointer border-default-primary border-2"
					>
						{{ selectedRegion }}
					</ListboxButton>
					<ListboxOptions class="absolute z-10 mt-1 w-full bottom-full">
						<ListboxOption
							v-for="region in regions"
							:key="region"
							:value="region"
							class="cursor-pointer py-2 px-2 text-white hover:brightness-200 bg-default-secondary border-default-primary border-2"
						>
							{{ region }}
						</ListboxOption>
					</ListboxOptions>
				</Listbox>
				<input
					v-model="gameName"
					type="text"
					placeholder="Enter game name"
					class="min-w-24 py-2 px-2 bg-default-secondary border-2 border-default-primary text-white placeholder:text-gray-400"
				/>
				<div class="flex flex-row flex-nowrap items-center border-default-primary border-2 bg-default-secondary pl-2 min-w-24">
					<p class="text-white text-2xl mr-2">#</p>
					<input v-model="tagLine" type="text" placeholder="tagline" class="min-w-24 py-2 px-2 text-white placeholder:text-gray-400" />
				</div>

				<button
					@click="enterRegions"
					class="p-2 text-white rounded-lg hover:brightness-200 cursor-pointer bg-default-secondary border-default-primary border-2"
				>
					GO
				</button>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { Listbox, ListboxButton, ListboxOptions, ListboxOption } from "@headlessui/vue"
const playerDataStore = usePlayerDataStore()

const regions = ["americas", "asia", "europe"]
const selectedRegion = ref("americas")
const gameName = ref("")
const tagLine = ref("")

const emit = defineEmits(["close_modal"])
const enterRegions = async () => {
	try {
		if (gameName.value.trim() === "" || tagLine.value.trim() === "") {
			alert("Please enter both game name and tagline.")
			return
		}

		const response = await $fetch(
			`/api/player?gameName=${encodeURIComponent(gameName.value)}&tagLine=${encodeURIComponent(tagLine.value)}&region=${selectedRegion.value}`,
			{
				method: "GET",
			}
		)
		console.log(response)

		if (!Object.keys(response).find((key) => key === "content")) {
			alert(response.statusMessage)
			return
		}
		if (response.content == "") {
			alert(`${response.statusMessage} Please come back in an hour while we crank the numbers.`)
			return
		}
		// found player data
		playerDataStore.playerData = response.content.applicationStats
		emit("close_modal")
	} catch (error) {
		alert("Error during player fetching: " + error)
		return
	}
}
</script>
