<template>
	<div class="relative w-full overflow-hidden">
		<div class="flex">
			<div v-for="(card, index) in displayCards" :key="index" class="flex-shrink-0 p-2" :style="{ width: `${100 / 3}%` }">
				<div class="bg-white text-center border">
					<component :is="card" />
				</div>
			</div>
		</div>

		<button v-if="totalCards > 3" @click="prevSlide" class="absolute left-2 top-1/2 -translate-y-1/2">
			<ChevronLeftIcon class="stroke-black stroke-2 size-8" />
		</button>
		<button v-if="totalCards > 3" @click="nextSlide" class="absolute right-2 top-1/2 -translate-y-1/2">
			<ChevronRightIcon class="stroke-black stroke-2 size-8" />
		</button>
	</div>
</template>

<script setup lang="ts">
import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/vue/16/solid"

const slots = useSlots()
const allCards = slots.default?.() || []
const totalCards = allCards.length

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
