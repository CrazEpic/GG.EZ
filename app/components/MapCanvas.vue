<template>
	<div ref="pixiContainer" class="border-black border-2"></div>
</template>

<script setup lang="ts">
const pixiContainer = useTemplateRef("pixiContainer")
const emit = defineEmits(["change_modal"])
const pixi = usePixiStore()

onMounted(async () => {
	await pixi.initPixi(pixiContainer.value!)

	pixi.viewport?.on("pointerup", (event: any) => {
		const screen = event.data.global
		const worldPoint = pixi.viewport!.toWorld(screen.x, screen.y)
		pixi.focusOn(worldPoint.x, worldPoint.y, () => {
			emit("change_modal", "FRELJORD")
		})
	})
})
</script>
