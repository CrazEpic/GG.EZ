import { defineStore } from "pinia"
import { ref } from "vue"
import { Application, Assets, Sprite, Texture, Color } from "pixi.js"
import { Viewport } from "pixi-viewport"
import { gsap } from "gsap"

export const usePixiStore = defineStore("pixi", () => {
	const app = ref<Application | null>(null)
	const viewport = ref<Viewport | null>(null)
	const fadeOverlay = ref<Sprite | null>(null)

	const worldWidth = 1528
	const worldHeight = 900

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

		// Base map
		const mapTexture = await Assets.load("RuneterraMap.png")
		const map = vp.addChild(new Sprite(mapTexture))
		map.width = worldWidth
		map.height = worldHeight

		// Fade overlay
		const fade = vp.addChild(new Sprite(Texture.WHITE))
		fade.width = worldWidth
		fade.height = worldHeight
		fade.zIndex = 10
		fade.position.set(0, 0)
		fade.tint = new Color({ r: 0, g: 0, b: 0 })
		fade.alpha = 0
		fadeOverlay.value = fade
	}

	/** Move and zoom to a specific point */
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

		if (fadeOverlay.value) {
			gsap.to(fadeOverlay.value, { duration: 1, alpha: 1 })
		}
	}

	/** Reset camera and remove fade */
	const resetCamera = async () => {
		if (!viewport.value) return
		viewport.value.animate({
			time: 800,
			position: { x: worldWidth / 2, y: worldHeight / 2 },
			scale: 1,
			ease: "easeOutSine",
		})

		if (fadeOverlay.value) {
			gsap.to(fadeOverlay.value, { duration: 0.8, alpha: 0 })
		}
	}

	return {
		app,
		viewport,
		fadeOverlay,
		worldWidth,
		worldHeight,
		initPixi,
		focusOn,
		resetCamera,
	}
})
