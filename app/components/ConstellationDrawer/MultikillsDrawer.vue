<template>
<div class="flex flex-col items-center px-10 text-white text-cinzel">
    <h1 class="text-3xl py-5">THE EMPRESS</h1>
    <div class="relative">
    <img src="/eternals/Empress.png" class="w-50 h-50" />
    <img src="/eternals/IconFrame.png" class="w-50 h-50 absolute inset-0" />
    </div>
    <p class="text-md py-5">"The weak multiply. The strong prevail."</p>
    <h2 class="text-xl py-6">Solo Kills</h2>
    <p>{{ soloKills }}</p>
    <h2 class="text-xl py-6">Double Kills</h2>
    <p>{{ doubleKills }}</p>
    <h2 class="text-xl py-6">Triple Kills</h2>
    <p>{{ soloKills }}</p>
    <h2 class="text-xl py-6">Quadra Kills</h2>
    <p>{{ soloKills }}</p>
    <h2 class="text-xl py-6">Pentakills</h2>
    <p>{{ soloKills }}</p>
</div>
</template>

<script setup lang='ts'>
const playerDataStore = usePlayerDataStore()
const soloKills = playerDataStore.playerData?.sr.targon_info.solo_kills
const doubleKills = playerDataStore.playerData?.sr.targon_info.double_kills
const tripleKills = playerDataStore.playerData?.sr.targon_info.triple_kills
const quadraKills = playerDataStore.playerData?.sr.targon_info.quadra_kills
const pentaKills = playerDataStore.playerData?.sr.targon_info.penta_kills

defineProps({
        soloKills : Number,
        doubleKills : Number,
        tripleKills : Number,
        quadraKills : Number,
        pentaKills : Number,
    })
</script>