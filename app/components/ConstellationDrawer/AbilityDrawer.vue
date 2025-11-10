<template>
<div class="flex flex-col items-center px-10 text-white text-cinzel">
    <h1 class="text-3xl py-5">THE EVOKER</h1>
    <div class="relative">
    <img src="/eternals/Evoker.png" class="w-50 h-50" />
    <img src="/eternals/IconFrame.png" class="w-50 h-50 absolute inset-0" />
    </div>
    <p class="text-md py-5">"Mastery comes from honing every skill."</p>
    <h2 class="text-xl py-20">Ability Count</h2>
    <div class="relative w-80 h-80">
  
  <div class="absolute top-0 left-0 flex flex-col items-center">
    <img :src="`/champ-abilities/${champion}Q.png`" class="w-25 h-25"/>
    <p class="text-white font-bold">Q: {{ qCast }}</p>
  </div>
  
  <div class="absolute top-0 right-0 flex flex-col items-center">
    <img :src="`/champ-abilities/${champion}W.png`" class="w-25 h-25"/>
    <p class="text-white font-bold">W: {{ wCast }}</p>
  </div>
  
  <div class="absolute bottom-0 left-0 flex flex-col items-center">
    <img :src="`/champ-abilities/${champion}E.png`" class="w-25 h-25"/>
    <p class="text-white font-bold">E: {{ eCast }}</p>
  </div>

  <div class="absolute bottom-0 right-0 flex flex-col items-center">
    <img :src="`/champ-abilities/${champion}R.png`" class="w-25 h-25"/>
    <p class="text-white font-bold">R: {{ rCast }}</p>
  </div>
</div>
</div>
</template>

<script setup lang='ts'>
const playerDataStore = usePlayerDataStore()
const champion = playerDataStore.playerData?.sr.targon_info.most_played_champion[0]
const qCast = playerDataStore.playerData?.sr.targon_info.q_ability_casts
const wCast = playerDataStore.playerData?.sr.targon_info.w_ability_casts
const eCast = playerDataStore.playerData?.sr.targon_info.e_ability_casts
const rCast = playerDataStore.playerData?.sr.targon_info.r_ability_casts

defineProps({
        champion : String,
        qCast : Number,
        wCast : Number,
        eCast : Number,
        rCast : Number,
    })
</script>