<template>
	<div class="flex flex-col items-center px-10 text-white text-cinzel">
		<h1 class="text-3xl py-5">THE FORGEMASTER</h1>
		<div class="relative">
			<img src="/eternals/Forgemaster.png" class="w-50 h-50" />
			<img src="/eternals/IconFrame.png" class="w-50 h-50 absolute inset-0" />
		</div>
		<p class="text-md py-5">"The tools you choose today are the shields you wield tomorrow.."</p>
		<h2 class="text-xl py-10">Build</h2>
		<div class="relative w-80 h-80">
			<div class="flex flex-col items-center mt-5">
				<!-- Keystone -->
				<div class="flex flex-col items-center mb-4">
					<img :src="`rune-icons/keystones/${keystone}.png`" class="w-16 h-16" />
					<span class="text-white">{{ keystoneCount }}</span>
				</div>

				<!-- Summoner Spells -->
				<div class="flex gap-4 mb-4">
					<div class="flex flex-col items-center">
						<img :src="`/summoner-spells/${summonerSpell1[0]}.png`" class="w-16 h-16" />
						<span class="text-white">{{ summonerSpell1[1] }}</span>
					</div>
					<div class="flex flex-col items-center">
						<img :src="`/summoner-spells/${summonerSpell2[0]}.png`" class="w-16 h-16" />
						<span class="text-white">{{ summonerSpell2[1] }}</span>
					</div>
				</div>

				<div class="flex gap-4">
					<div class="flex flex-col items-center">
						<img :src="`/items/${firstItem[0]}.png`" class="w-16 h-16" />
						<span class="text-white">{{ firstItem[1] }}</span>
					</div>
					<div class="flex flex-col items-center">
						<img :src="`/items/${secondItem[0]}.png`" class="w-16 h-16" />
						<span class="text-white">{{ secondItem[1] }}</span>
					</div>
					<div class="flex flex-col items-center">
						<img :src="`/items/${thirdItem[0]}.png`" class="w-16 h-16" />
						<span class="text-white">{{ thirdItem[1] }}</span>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
const playerDataStore = usePlayerDataStore()
const keystone = playerDataStore.playerData?.sr.targon_info.most_used_keystone_rune[0]
const keystoneCount = playerDataStore.playerData?.sr.targon_info.most_used_keystone_rune[1]
const summonerSpell1 = playerDataStore.playerData?.sr.targon_info.top_2_summoner_spells[0]
const summonerSpell2 = playerDataStore.playerData?.sr.targon_info.top_2_summoner_spells[1]
const firstItem = playerDataStore.playerData?.sr.targon_info.top_3_items[0]
const secondItem = playerDataStore.playerData?.sr.targon_info.top_3_items[1]
const thirdItem = playerDataStore.playerData?.sr.targon_info.top_3_items[2]

defineProps({
	keystone: Number,
	summonerSpell1: Array,
	summonerSpell2: Array,
	firstItem: Array,
	secondItem: Array,
	thirdItem: Array,
})
</script>
