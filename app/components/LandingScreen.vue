<template>
	<div style="background-color: rgba(0, 0, 0, 0.75)">
		<Header class="sticky top-0"></Header>
		<p class="text-white">
			GG.EZ was created under Riot Games' "Legal Jibber Jabber" policy using assets owned by Riot Games. Riot Games does not endorse or sponsor this
			project.
		</p>
		<button class="text-white cursor-pointer" @click="enterRegions">Get started</button>
	</div>
</template>

<script setup lang="ts">
const playerDataStore = usePlayerDataStore()

const emit = defineEmits(["close_modal"])
const enterRegions = async () => {
	const response = await $fetch("/api/player")
	playerDataStore.playerData = response
	emit("close_modal")
}
</script>
