<template>
    <p class="text-white text-md">PICK A CARD TO COLLECT</p>
    <Carousel class="my-8">
        <CardStat v-for="(stat, index) in stats" :key="index" :borderColor="borderColor" :title="stat.title" :value="stat.value" />
    </Carousel>
</template>

<script setup lang="ts">
const props = defineProps({
    borderColor: String,
    stats: Array,
})
</script>