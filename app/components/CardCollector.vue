<template>
    <p class="text-white text-md">PICK A CARD TO COLLECT</p>
            <Carousel class="my-8">
                <p :class="['h-full', 'flex', 'items-center', 'justify-center', 'text-white', borderColor, 'border-2']">{{stat1}}</p>
                <p :class="['h-full', 'flex', 'items-center', 'justify-center', 'text-white', borderColor, 'border-2']">{{stat2}}</p>
                <p :class="['h-full', 'flex', 'items-center', 'justify-center', 'text-white', borderColor, 'border-2']">{{stat3}}</p>
                <p :class="['h-full', 'flex', 'items-center', 'justify-center', 'text-white', borderColor, 'border-2']">{{stat4}}</p>
                <p :class="['h-full', 'flex', 'items-center', 'justify-center', 'text-white', borderColor, 'border-2']">{{stat5}}</p>
                <p :class="['h-full', 'flex', 'items-center', 'justify-center', 'text-white', borderColor, 'border-2']">{{stat6}}</p>
            </Carousel>
</template>

<script setup lang="ts">
    defineProps({
        borderColor: String,
        statsTitle: String,
        stat1: String,
        stat2: String,
        stat3: String,
        stat4: String,
        stat5: String,
        stat6: String,
    })

</script>