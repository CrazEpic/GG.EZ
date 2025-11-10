<template>
    <p class="text-white text-md">PICK A CARD TO COLLECT</p>
    <SmallerRegionSharedCarousel :minCardWidth="320" class="my-8">
        <SmallerRegionSharedCardStat v-for="(stat, index) in stats" :key="index" :borderColor="borderColor" :title="stat.title" :value="stat.value" :showGraph="stat.showGraph" :graphType="stat.graphType" :graphData="stat.graphData" :graphLabels="stat.graphLabels" :graphColors="stat.graphColors" :topItems="stat.topItems"/>
    </SmallerRegionSharedCarousel>
</template>

<script setup lang="ts">
const props = defineProps({
    borderColor: String,
    stats: Array,
})
</script>