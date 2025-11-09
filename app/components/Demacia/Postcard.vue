<!-- Postcard.vue -->
<template>
	<div class="flex flex-col items-center space-y-4">
		<!-- I think html2canvas doesn't like tailwind -->
		<div ref="postcardRef" style="width: 360px; height: 640px; border-width: 2px; border-color: #c28f2c; background-color: #111111">
			<div style="height: 192px; position: relative">
				<!-- Champion Image as background -->
				<div style="width: 100%; height: 100%; position: absolute; overflow: hidden">
					<img src="/champion-constellation/Aatrox_0.png" style="width: 100%; height: 100%; object-fit: cover" />
				</div>
				<!-- Overlay content -->
				<div
					style="position: relative; display: flex; flex-direction: column; gap: 2px; color: white; height: 100%; justify-content: end; padding: 16px"
				>
					<div class="flex flex-row gap-2 items-end">
						<img src="/dan_the_penguin.png" class="w-16 h-16 rounded-full border-2 border-[#FFFFFF]" />
						<div class="flex flex-col justify-end">
							<p class="text-left">2025 GG.EZ</p>
							<p class="whitespace-nowrap">Dan the Penguin</p>
							<p class="whitespace-nowrap">#NA1</p>
						</div>
					</div>

					<div class="flex flex-row gap-2">
						<div class="border-2 border-white bg-default-secondary px-2 py-1">
							<p class="whitespace-nowrap">Games 500</p>
						</div>
						<div class="border-2 border-white bg-default-secondary px-2 py-1">
							<p class="whitespace-nowrap">Winrate 52%</p>
						</div>
					</div>
				</div>
			</div>
			<div class="h-[448px]">
				<div
					:style="{
						gridTemplateColumns: 'repeat(4, 1fr)',
						gridTemplateRows: 'repeat(6, 1fr)',
						display: 'grid',
						gap: '2px',
						padding: '16px',
						height: '100%',
					}"
				>
					<DemaciaTile v-for="tile in filledGrid" :key="tile.id" v-bind="tile" />
				</div>
			</div>
		</div>

		<button @click="exportPostcard" class="px-4 py-2 border-2 border-default-primary bg-default-secondary text-white hover:brightness-200">
			Export PNG
		</button>
	</div>
</template>

<script setup>
import html2canvas from "html2canvas"
const postcardRef = useTemplateRef("postcardRef")

const tiles = ref([
	{ id: 1, type: "text", text: "Hello World", colSpan: 2, rowSpan: 1, gridColumnStart: 1, gridRowStart: 1 },
	{ id: 2, type: "percentage", percentage: 75, colSpan: 1, rowSpan: 1, gridColumnStart: 3, gridRowStart: 1 },
	{ id: 3, type: "map", mapData: { region: "North" }, colSpan: 2, rowSpan: 2, gridColumnStart: 2, gridRowStart: 3 },
	// { id: 4, type: "image", image: "/images/sticker.png", colSpan: 1, rowSpan: 1 },
	// Add more tiles as needed
])
const totalRows = 6
const totalCols = 4

const filledGrid = computed(() => {
	// Include all original tiles
	const realTiles = tiles.value.map((t) => ({
		...t,
	}))

	// Fill empty spots
	const emptyTiles = []
	for (let row = 1; row <= totalRows; row++) {
		for (let col = 1; col <= totalCols; col++) {
			const occupied = realTiles.some(
				(t) =>
					row >= t.gridRowStart && row < t.gridRowStart + (t.rowSpan || 1) && col >= t.gridColumnStart && col < t.gridColumnStart + (t.colSpan || 1)
			)
			if (!occupied) {
				emptyTiles.push({
					id: `empty-${row}-${col}`,
					type: "empty",
					gridRowStart: row,
					gridColumnStart: col,
					rowSpan: 1,
					colSpan: 1,
				})
			}
		}
	}

	return [...realTiles, ...emptyTiles]
})

const exportPostcard = () => {
	html2canvas(postcardRef.value, {
		scale: (1080 / postcardRef.value.offsetWidth) * window.devicePixelRatio, // keep your 1080p export scale
		useCORS: true,
		allowTaint: true,
	}).then((canvas) => {
		const link = document.createElement("a")
		link.download = "postcard.png"
		link.href = canvas.toDataURL("image/png")
		link.click()
	})
}
</script>
