<template>
	<div>
		<form @submit.prevent="fetchRiotAccountInfo">
			<input type="text" v-model="riotAccountInfoGameName" placeholder="Enter gamename here" />
			<input type="text" v-model="riotAccountInfoTagline" placeholder="Enter tagline here" />
			<button type="submit" class="border-black border-2 cursor-pointer">Fetch Riot Account Info</button>
		</form>
		<div v-if="riotAccountInfo">
			<h2>Riot Account Info:</h2>
			<div>{{ riotAccountInfo }}</div>
		</div>
	</div>
</template>

<script setup lang="ts">
const riotAccountInfoGameName = ref()
const riotAccountInfoTagline = ref()
const riotAccountInfo = ref()

const fetchRiotAccountInfo = async () => {
	try {
		const data = await $fetch("/api/account", {
			query: { gameName: riotAccountInfoGameName.value, tagLine: riotAccountInfoTagline.value },
		})
		riotAccountInfo.value = data
	} catch (error) {
		console.error("Error fetching Riot account info:", error)
	}
}
</script>
