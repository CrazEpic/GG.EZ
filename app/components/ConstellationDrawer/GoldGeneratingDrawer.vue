<template>
<div class="flex flex-col items-center px-10 text-white text-cinzel">
    <h1 class="text-3xl py-5">THE COLLECTOR</h1>
    <div class="relative">
    <img src="/eternals/Collector.png" class="w-50 h-50" />
    <img src="/eternals/IconFrame.png" class="w-50 h-50 absolute inset-0" />
    </div>
    <p class="text-md py-8">"Fortune favors the wealthy."</p>
    <h2 class="text-xl pt-5 pb-10">Total Gold Generated</h2>
    <div>
        <img src="/drawers-icon/Coins_Icon.png" class="w-10 h-10" />
        <p>{{ goldEarned }}</p>
    </div>
    
    <h2 class="text-xl py-10">Total Minion Kills</h2>    
    <div>
        <img src="/drawers-icon/Minion_icon.png" class="w-10 h-10" />
        <p>{{ minionsKilled }}</p>
    </div>

    <h2 class="text-xl py-10">Total Jungle Minion Kills</h2>
    <div>
        <img src="/drawers-icon/Monster_icon.png" class="w-10 h-10" />
        <p>{{ jungleMinionsKilled }}</p>
    </div>
</div>
</template>

<script setup lang='ts'>
const playerDataStore = usePlayerDataStore()
const goldEarned = playerDataStore.playerData?.sr.targon_info.gold_earned
const jungleMinionsKilled = playerDataStore.playerData?.sr.targon_info.jungle_minions_killed
const minionsKilled = playerDataStore.playerData?.sr.targon_info.minions_killed

defineProps({
        goldEarned : Number,
        jungleMinionsKilled : Number,
        minionsKilled : Number
    })
</script>