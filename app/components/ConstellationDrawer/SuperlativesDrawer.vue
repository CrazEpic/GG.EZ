<template>
<div class="flex flex-col items-center px-10 text-white text-cinzel">
    <h1 class="text-3xl py-5">THE CHAMPION</h1>
    <div class="relative">
    <img :src="`/champ-icons/${champion}.png`" class="w-50 h-50 rounded-full" />
    <img src="/eternals/IconFrame.png" class="w-50 h-50 absolute inset-0" />
    </div>
    <!-- <p class="text-md py-5">"Champion Quote"</p> -->
    <hr class="w-full border-2 border-[#C28F2C] my-4" />

    <div class="flex flex-col mb-20">
    <h1 class="text-3xl p-10">Highest Winstreak</h1>
    <h2 class="text-3xl">{{ highestWinstreak }}</h2>
    </div>

    <div class="flex flex-col">
    <h1 class="text-3xl p-10">PEAK KDA</h1>
    <h2 class="text-3xl">{{ peakKDA }}</h2>
    </div>

    <div class='text-white'>
        {{ championMastery }}
    </div>

</div>
</template>

<script setup lang='ts'>
import championKeyToName from '~/assets/data/champion_key_to_name'

const playerDataStore = usePlayerDataStore()
const champion = playerDataStore.playerData?.sr.targon_info.most_played_champion[0]
const highestWinstreak = playerDataStore.playerData?.sr.targon_info.highest_winstreak
const peakKDA = Number(playerDataStore.playerData?.sr.targon_info.highest_kda.toFixed(2))

const championMastery = ref(0)
onMounted(() =>{
    const championNumber = Object.keys(championKeyToName).find((key) =>{
        return championKeyToName[key]['Id'] == champion
    })
    console.log(champion)
    const response = $fetch(`/api/championMastery?puuid=${playerDataStore.playerData?.puuid}&championId=${championNumber}`)
    championMastery.value = response.championPoints
}) 

defineProps({
    champion : String,
    highestWinstreak : Number,
    peakKDA : Number,
    })
</script>