<template>
	<div class="relative w-full overflow-hidden" ref="carouselContainer">
		<div class="flex gap-4 justify-center items-center w-full flex-nowrap">
			<template v-for="(card, index) in displayCards" :key="index">
				<!-- filler space cards -->
				<div v-if="!card" :class="`grow basis-${minCardWidth}px w-full`">
					<div class="h-90 w-full"></div>
				</div>
				<!-- real card -->
				<div v-else :class="`grow basis-${minCardWidth}px w-full`">
					<div class="bg-black text-center border h-110 w-min mx-auto">
						<component :is="card" />
					</div>
				</div>
			</template>
		</div>

		<!-- Navigation buttons -->
		<button v-if="totalCards > 1" @click="prevSlide" class="absolute left-2 top-1/2 -translate-y-1/2">
			<ChevronLeftIcon class="stroke-white stroke-2 size-8" />
		</button>
		<button v-if="totalCards > 1" @click="nextSlide" class="absolute right-2 top-1/2 -translate-y-1/2">
			<ChevronRightIcon class="stroke-white stroke-2 size-8" />
		</button>
	</div>
</template>

<script setup lang="ts">
import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/vue/16/solid"
import { Fragment, ref, computed, onMounted, onBeforeUnmount, useSlots } from "vue"

const props = defineProps({
	minCardWidth: { type: Number, required: true },
})

const carouselContainer = useTemplateRef("carouselContainer")
const slots = useSlots()

// Flatten slot VNodes in case of fragments
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

const currentIndex = ref(Math.trunc(totalCards / 2))
const visibleMode = ref("single")

const updateVisibleMode = () => {
	if (!carouselContainer.value) return
	const containerWidth = carouselContainer.value.clientWidth
	visibleMode.value = containerWidth > props.minCardWidth * 3 ? "three" : "single"
}

const displayCards = computed(() => {
	if (visibleMode.value === "single") {
		if (totalCards === 0) return [null]
		const centerCard = allCards[currentIndex.value % totalCards]
		return [centerCard]
	}

	// visibleMode === "three"
	if (totalCards === 0) return [null, null, null]
	if (totalCards === 1) return [null, allCards[0], null]
	if (totalCards === 2) {
		const left = allCards[currentIndex.value % 2]
		const right = allCards[(currentIndex.value + 1) % 2]
		return [null, left, right]
	}

	const prev = allCards[(currentIndex.value - 1 + totalCards) % totalCards]
	const curr = allCards[currentIndex.value % totalCards]
	const next = allCards[(currentIndex.value + 1) % totalCards]
	return [prev, curr, next]
})

const nextSlide = () => {
	currentIndex.value = (currentIndex.value + 1) % totalCards
}

const prevSlide = () => {
	currentIndex.value = (currentIndex.value + totalCards - 1) % totalCards
}

onMounted(() => {
	updateVisibleMode()
	window.addEventListener("resize", updateVisibleMode)
})

onBeforeUnmount(() => {
	window.removeEventListener("resize", updateVisibleMode)
})
</script>