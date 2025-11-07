<template>
    <div class="relative w-full overflow-hidden">
        <div class="flex flex-wrap justify-center space-x-4">
            <div v-for="(card, index) in displayCards" :key="index" class="shrink-0 p-2">
                <div class="bg-black text-center border h-90 w-72">
                    <component :is="card" />
                </div>
            </div>
        </div>

        <button v-if="totalCards > 3" @click="prevSlide" class="absolute left-2 top-1/2 -translate-y-1/2">
            <ChevronLeftIcon class="stroke-white stroke-2 size-8" />
        </button>
        <button v-if="totalCards > 3" @click="nextSlide" class="absolute right-2 top-1/2 -translate-y-1/2">
            <ChevronRightIcon class="stroke-white stroke-2 size-8" />
        </button>
    </div>
</template>

<script setup lang="ts">
import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/vue/16/solid"
import { Fragment } from "vue"

const slots = useSlots()

// if you use v-for, vue creates an outermost fragment
const flattenVNodes = (vnodes) => {
    const result = []
    vnodes.forEach((vnode) => {
        if (!vnode) return
        if (vnode.type === Fragment && Array.isArray(vnode.children)) {
            result.push(...flattenVNodes(vnode.children))
        } else {
            result.push(vnode)
        }
    })
    return result
}

const raw = slots.default?.() ?? []
const allCards = flattenVNodes(raw)
const totalCards = allCards.length
console.log(totalCards)

const currentIndex = ref(Math.trunc(totalCards / 2))

const displayCards = computed(() => {
    if (totalCards <= 3) return allCards
    return [allCards[(currentIndex.value + totalCards - 1) % totalCards], allCards[currentIndex.value], allCards[(currentIndex.value + 1) % totalCards]]
})

const nextSlide = () => {
    currentIndex.value = (currentIndex.value + 1) % totalCards
}

const prevSlide = () => {
    currentIndex.value = (currentIndex.value + totalCards - 1) % totalCards
}
</script>