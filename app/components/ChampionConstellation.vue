<template>
	<div ref="championConstellationContainer" class="border-black border-2"></div>
</template>

<script setup lang="ts">
import { Application, Assets, Graphics, Sprite, Texture } from "pixi.js"
import { Viewport } from "pixi-viewport"
import championsStarCoords from "~/assets/data/championCoordinates"

const props = defineProps({
	champion: {
		type: String,
		required: true,
	},
})

const pixiContainer = useTemplateRef("championConstellationContainer")

const app = ref<Application | null>(null)
const viewport = ref<Viewport | null>(null)

const worldWidth = 1215
const worldHeight = 717

const initPixi = async (container: HTMLElement) => {
	if (app.value) return // prevent re-init

	const pixiApp = new Application()
	await pixiApp.init({ background: "#000000", resizeTo: container })
	container.appendChild(pixiApp.canvas)
	app.value = pixiApp

	const vp = new Viewport({
		screenWidth: container.clientWidth,
		screenHeight: container.clientHeight,
		worldWidth,
		worldHeight,
		events: pixiApp.renderer.events,
	})
	pixiApp.stage.addChild(vp)

	vp.drag()
		.pinch()
		.wheel()
		.decelerate({ friction: 0.95 })
		.clamp({
			direction: "all",
			left: 0,
			top: 0,
			right: worldWidth,
			bottom: worldHeight,
			underflow: "center",
		})
		.clampZoom({
			minWidth: worldWidth / 5,
			maxWidth: worldWidth,
			minHeight: worldHeight / 5,
			maxHeight: worldHeight,
		})

	vp.moveCenter(worldWidth / 2, worldHeight / 2)
	viewport.value = vp

	const championConstellationArtTexture = await Assets.load(`champion-constellation/${props.champion}.png`)
	const championConstellationArt = vp.addChild(new Sprite(championConstellationArtTexture))
	championConstellationArt.width = worldWidth
	championConstellationArt.height = worldHeight

	// stars
	const starCoordinates = championsStarCoords[`${props.champion}`]
	const edges = new Set()
	const stars = {}
	const starWidth = 50
	const starHeight = 50
	Object.keys(starCoordinates).forEach((starNumber) => {
		const newStar = vp.addChild(new Sprite(Texture.WHITE))
		newStar.width = starWidth
		newStar.height = starHeight
		newStar.label = starNumber
		newStar.x = starCoordinates[starNumber]["x"]
		newStar.y = starCoordinates[starNumber]["y"]
		stars[starNumber] = newStar
		// order neighbor so smaller number is first
		starCoordinates[starNumber].neighbors.forEach((neighbor) => {
			edges.add(`${Math.min(starNumber, neighbor)}-${Math.max(starNumber, neighbor)}`)
		})
	})

	const edgeGraphics = new Graphics()
	vp.addChild(edgeGraphics)

	edges.forEach((edge) => {
		const [a, b] = edge.split("-")
		const starA = stars[a]
		const starB = stars[b]
		edgeGraphics.moveTo(starA.x + starWidth / 2, starA.y + starHeight / 2)
		edgeGraphics.lineTo(starB.x + starWidth / 2, starB.y + starHeight / 2)
		edgeGraphics.stroke({ width: 10, color: 0xffffff }) // Finalize the line drawing
	})

	vp.on("pointerdown", (event) => {
		const screen = event.global
		const worldPoint = vp.toWorld(screen.x, screen.y)
		const clickedChildren = vp.children.find((child) => {
			return (
				Object.keys(starCoordinates).includes(child.label) &&
				child.x <= worldPoint.x &&
				worldPoint.x <= child.x + child.width &&
				child.y <= worldPoint.y &&
				worldPoint.y <= child.y + child.height
			)
		})
		if (clickedChildren) {
			console.log(clickedChildren.label)
		}
	})
}

const resetCamera = async () => {
	if (!viewport.value) return
	viewport.value.animate({
		time: 800,
		position: { x: worldWidth / 2, y: worldHeight / 2 },
		scale: 1,
		ease: "easeOutSine",
	})
}

const handleWheel = (e: WheelEvent) => {
	if (pixiContainer.value!.contains(e.target as Node)) e.preventDefault()
}

const handleTouchMove = (e: TouchEvent) => {
	if (pixiContainer.value!.contains(e.target as Node)) e.preventDefault()
}

onMounted(async () => {
	await initPixi(pixiContainer.value!)

	// use { passive: false } so preventDefault works
	window.addEventListener("wheel", handleWheel, { passive: false })
	window.addEventListener("touchmove", handleTouchMove, { passive: false })
})

onBeforeUnmount(() => {
	window.removeEventListener("wheel", handleWheel)
	window.removeEventListener("touchmove", handleTouchMove)
})
</script>
