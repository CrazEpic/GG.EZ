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

const emit = defineEmits(["change_drawer"])
const pixiContainer = useTemplateRef("championConstellationContainer")

const app = ref<Application | null>(null)
const viewport = ref<Viewport | null>(null)

const worldWidth = 1215
const worldHeight = 717

const resetCamera = async () => {
	if (!viewport.value) return
	viewport.value.animate({
		time: 800,
		position: { x: worldWidth / 2, y: worldHeight / 2 },
		scale: 1,
		ease: "easeOutSine",
	})
}

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

	const championConstellationArtTexture = await Assets.load(`champion-constellation/${props.champion}_0.png`)
	const championConstellationArt = vp.addChild(new Sprite(championConstellationArtTexture))
	championConstellationArt.width = worldWidth
	championConstellationArt.height = worldHeight

	// stars
	const newStarTexture = await Assets.load("stars/star1.png")
	const starCoordinates = championsStarCoords[`${props.champion}`]
	const edges = new Set()
	const stars = {}
	const starWidth = 20
	const starHeight = 20
	Object.keys(starCoordinates).forEach((starNumber) => {
		const newStar = vp.addChild(new Sprite(newStarTexture))
		newStar.width = starWidth
		newStar.height = starHeight
		newStar.label = starNumber
		newStar.anchor.set(0.5)
		newStar.scale.set(0.1)
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
		edgeGraphics.moveTo(starA.x, starA.y)
		edgeGraphics.lineTo(starB.x, starB.y)
		edgeGraphics.stroke({ width: 1, color: 0xffffff }) // Finalize the line drawing
	})

	vp.on("pointermove", (event) => {
		const screen = event.global
		const worldPoint = vp.toWorld(screen.x, screen.y)
		const hoveredChildren = vp.children.find((child) => {
			return (
				Object.keys(starCoordinates).includes(child.label) &&
				child.x - child.width / 2 <= worldPoint.x &&
				worldPoint.x <= child.x + child.width / 2 &&
				child.y - child.height / 2 <= worldPoint.y &&
				worldPoint.y <= child.y + child.height / 2
			)
		})
		if (hoveredChildren) {
			hoveredChildren.width = 30
			hoveredChildren.height = 30
		} else {
			stars["1"].width = 20
			stars["1"].height = 20
			stars["2"].width = 20
			stars["2"].height = 20
			stars["3"].width = 20
			stars["3"].height = 20
			stars["4"].width = 20
			stars["4"].height = 20
			stars["5"].width = 20
			stars["5"].height = 20
			stars["6"].width = 20
			stars["6"].height = 20
			stars["7"].width = 20
			stars["7"].height = 20
		}
	})

	vp.on("pointerdown", (event) => {
		const screen = event.global
		const worldPoint = vp.toWorld(screen.x, screen.y)
		const clickedChildren = vp.children.find((child) => {
			return (
				Object.keys(starCoordinates).includes(child.label) &&
				child.x - child.width / 2 <= worldPoint.x &&
				worldPoint.x <= child.x + child.width / 2 &&
				child.y - child.height / 2 <= worldPoint.y &&
				worldPoint.y <= child.y + child.height / 2
			)
		})
		if (clickedChildren) {
			switch (clickedChildren.label) {
				case "1":
					emit("change_drawer", "ABILITY", resetCamera, focusOn, clickedChildren.x, clickedChildren.y)
					break
				case "2":
					emit("change_drawer", "PLAYTIME", resetCamera, focusOn, clickedChildren.x, clickedChildren.y)
					break
				case "3":
					emit("change_drawer", "BUILD", resetCamera, focusOn, clickedChildren.x, clickedChildren.y)
					break
				case "4":
					emit("change_drawer", "GOLDGENERATING", resetCamera, focusOn, clickedChildren.x, clickedChildren.y)
					break
				case "5":
					emit("change_drawer", "KDADRAWER", resetCamera, focusOn, clickedChildren.x, clickedChildren.y)
					break
				case "6":
					emit("change_drawer", "MULTIKILLS", resetCamera, focusOn, clickedChildren.x, clickedChildren.y)
					break
				case "7":
					emit("change_drawer", "SUPERLATIVES", resetCamera, focusOn, clickedChildren.x, clickedChildren.y)
					break
			}
		}
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

const focusOn = (x: number, y: number, modalCallback?: () => void) => {
	if (!viewport.value) return
	const screenW = viewport.value.screenWidth ?? app.value?.screen.width
	const maxScale = screenW! / (worldWidth / 5)

	viewport.value.animate({
		time: 1000,
		position: { x, y },
		scale: maxScale,
		ease: "easeInOutSine",
		callbackOnComplete: modalCallback,
	})
}
</script>
