import { defineStore } from "pinia"
import { ref } from "vue"
import { Application, Assets, Sprite, Texture, Color } from "pixi.js"
import { Viewport } from "pixi-viewport"
import { gsap } from "gsap"
import { Text } from "pixi.js"

export const usePixiStore = defineStore("pixi", () => {
	const app = ref<Application | null>(null)
	const viewport = ref<Viewport | null>(null)
	const fadeOverlay = ref<Sprite | null>(null)

	const worldWidth = 1920
	const worldHeight = 919

	const initPixi = async (container: HTMLElement, changeModalEmit) => {
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
		fade.zIndex = 20
		fade.position.set(0, 0)
		fade.tint = new Color({ r: 0, g: 0, b: 0 })
		fade.alpha = 0
		fadeOverlay.value = fade

		// Freljord Icon
		const freljordTexture = await Assets.load("icons/freljord.png")
		const freljordHoverTexture = await Assets.load("hover-icons/freljord-hover.png")
		const freljordIcon = vp.addChild(new Sprite(freljordTexture))
		freljordIcon.x = 630
		freljordIcon.y = 210
		freljordIcon.zIndex = 10
		freljordIcon.height = 70
		freljordIcon.width = 70
		freljordIcon.roundPixels = true
		freljordIcon.label = "freljord"

		// Freljord Text
		const freljordText = new Text({
			text: "Freljord",
			style: {
				fontFamily: "Cinzel",
				fontSize: 26,
				fill: "#FFFFDE",
				stroke: {
					color: "#000000", // Black outline
					width: 2.5,
				},
				align: "center",
			},
		})
		freljordText.x = 620
		freljordText.y = 270
		vp.addChild(freljordText)

		// Freljord Terrain
		const freljordTerrain = await Assets.load("region-terrain/freljord.png")
		const freljordRegion = vp.addChild(new Sprite(freljordTerrain))
		freljordRegion.x = 218
		freljordRegion.y = -235
		freljordRegion.width = 1348
		freljordRegion.height = 1348
		freljordRegion.visible = false

		// Noxus Icon
		const noxusTexture = await Assets.load("icons/noxus.png")
		const noxusHoverTexture = await Assets.load("hover-icons/noxus-hover.png")
		const noxusIcon = vp.addChild(new Sprite(noxusTexture))
		noxusIcon.x = 850
		noxusIcon.y = 290
		noxusIcon.zIndex = 10
		noxusIcon.height = 70
		noxusIcon.width = 70
		noxusIcon.roundPixels = true
		noxusIcon.label = "noxus"

		// Noxus Text
		const noxusText = new Text({
			text: "Noxus",
			style: {
				fontFamily: "Cinzel",
				fontSize: 26,
				fill: "#FFFFDE",
				stroke: {
					color: "#000000", // Black outline
					width: 2.5,
				},
				align: "center",
			},
		})
		noxusText.x = 847
		noxusText.y = 350
		vp.addChild(noxusText)

		// Noxus Terrain
		const noxusTerrain = await Assets.load("region-terrain/noxus.png")
		const noxusRegion = vp.addChild(new Sprite(noxusTerrain))
		noxusRegion.x = 218
		noxusRegion.y = -235
		noxusRegion.width = 1348
		noxusRegion.height = 1348
		noxusRegion.visible = false

		// Ionia Icon
		const ioniaTexture = await Assets.load("icons/ionia.png")
		const ioniaHoverTexture = await Assets.load("hover-icons/ionia-hover.png")
		const ioniaIcon = vp.addChild(new Sprite(ioniaTexture))
		ioniaIcon.x = 1225
		ioniaIcon.y = 265
		ioniaIcon.zIndex = 10
		ioniaIcon.height = 70
		ioniaIcon.width = 70
		ioniaIcon.roundPixels = true
		ioniaIcon.label = "ionia"

		// ionia Text
		const ioniaText = new Text({
			text: "Ionia",
			style: {
				fontFamily: "Cinzel",
				fontSize: 26,
				fill: "#FFFFDE",
				stroke: {
					color: "#000000", // Black outline
					width: 2.5,
				},
				align: "center",
			},
		})
		ioniaText.x = 1232
		ioniaText.y = 325
		vp.addChild(ioniaText)

		// Ionia Terrain
		const ioniaTerrain = await Assets.load("region-terrain/ionia.png")
		const ioniaRegion = vp.addChild(new Sprite(ioniaTerrain))
		ioniaRegion.x = 219
		ioniaRegion.y = -235
		ioniaRegion.width = 1348
		ioniaRegion.height = 1348
		ioniaRegion.visible = false

		// Bilgewater Icon
		const bilgewaterTexture = await Assets.load("icons/bilgewater.png")
		const bilgewaterHoverTexture = await Assets.load("hover-icons/bilgewater-hover.png")
		const bilgewaterIcon = vp.addChild(new Sprite(bilgewaterTexture))
		bilgewaterIcon.x = 1245
		bilgewaterIcon.y = 520
		bilgewaterIcon.zIndex = 10
		bilgewaterIcon.height = 70
		bilgewaterIcon.width = 70
		bilgewaterIcon.roundPixels = true
		bilgewaterIcon.label = "bilgewater"

		// Bilgewater Text
		const bilgewaterText = new Text({
			text: "Bilgewater",
			style: {
				fontFamily: "Cinzel",
				fontSize: 26,
				fill: "#FFFFDE",
				stroke: {
					color: "#000000", // Black outline
					width: 2.5,
				},
				align: "center",
			},
		})
		bilgewaterText.x = 1230
		bilgewaterText.y = 575
		vp.addChild(bilgewaterText)

		// Bilgewater Terrain
		const bilgewaterTerrain = await Assets.load("region-terrain/bilgewater.png")
		const bilgewaterRegion = vp.addChild(new Sprite(bilgewaterTerrain))
		bilgewaterRegion.x = 219
		bilgewaterRegion.y = -235
		bilgewaterRegion.width = 1348
		bilgewaterRegion.height = 1348
		bilgewaterRegion.visible = false

		// Shadow Isles Icon
		const shadowIslesTexture = await Assets.load("icons/shadow-isles.png")
		const shadowIslesHoverTexture = await Assets.load("hover-icons/shadow-isles-hover.png")
		const shadowIslesIcon = vp.addChild(new Sprite(shadowIslesTexture))
		shadowIslesIcon.x = 1315
		shadowIslesIcon.y = 670
		shadowIslesIcon.zIndex = 10
		shadowIslesIcon.height = 70
		shadowIslesIcon.width = 70
		shadowIslesIcon.roundPixels = true
		shadowIslesIcon.label = "shadow_isles"

		// Shadow Isles Text
		const shadowIslesText = new Text({
			text: "Shadow Isles",
			style: {
				fontFamily: "Cinzel",
				fontSize: 26,
				fill: "#FFFFDE",
				stroke: {
					color: "#000000", // Black outline
					width: 2.5,
				},
				align: "center",
			},
		})
		shadowIslesText.x = 1280
		shadowIslesText.y = 730
		vp.addChild(shadowIslesText)

		// Shadow Isles Terrain
		const shadowIslesTerrain = await Assets.load("region-terrain/shadow-isles.png")
		const shadowIslesRegion = vp.addChild(new Sprite(shadowIslesTerrain))
		shadowIslesRegion.x = 219
		shadowIslesRegion.y = -235
		shadowIslesRegion.width = 1348
		shadowIslesRegion.height = 1348
		shadowIslesRegion.visible = false

		// Piltover & Zaun Icon
		const piltoverZaunTexture = await Assets.load("icons/piltover-zaun.png")
		const piltoverZaunHoverTexture = await Assets.load("hover-icons/piltover-zaun-hover.png")
		const piltoverZaunIcon = vp.addChild(new Sprite(piltoverZaunTexture))
		piltoverZaunIcon.x = 990
		piltoverZaunIcon.y = 452
		piltoverZaunIcon.height = 140
		piltoverZaunIcon.width = 70
		piltoverZaunIcon.roundPixels = true
		piltoverZaunIcon.label = "piltover_zaun"

		// Piltover & Zaun Text
		const piltoverZaunText = new Text({
			text: "Piltover & Zaun",
			style: {
				fontFamily: "Cinzel",
				fontSize: 26,
				fill: "#FFFFDE",
				stroke: {
					color: "#000000", // Black outline
					width: 2.5,
				},
				align: "center",
			},
		})
		piltoverZaunText.x = 830
		piltoverZaunText.y = 505
		vp.addChild(piltoverZaunText)

		// Ixtal Icon
		const ixtalTexture = await Assets.load("icons/ixtal.png")
		const ixtalHoverTexture = await Assets.load("hover-icons/ixtal-hover.png")
		const ixtalIcon = vp.addChild(new Sprite(ixtalTexture))
		ixtalIcon.x = 1050
		ixtalIcon.y = 630
		ixtalIcon.zIndex = 10
		ixtalIcon.height = 70
		ixtalIcon.width = 70
		ixtalIcon.roundPixels = true
		ixtalIcon.label = "ixtal"

		// Ixtal Text
		const ixtalText = new Text({
			text: "Ixtal",
			style: {
				fontFamily: "Cinzel",
				fontSize: 26,
				fill: "#FFFFDE",
				stroke: {
					color: "#000000", // Black outline
					width: 2.5,
				},
				align: "center",
			},
		})
		ixtalText.x = 1060
		ixtalText.y = 690
		vp.addChild(ixtalText)

		// Ixtal Terrain
		const ixtalTerrain = await Assets.load("region-terrain/ixtal.png")
		const ixtalRegion = vp.addChild(new Sprite(ixtalTerrain))
		ixtalRegion.x = 219
		ixtalRegion.y = -235
		ixtalRegion.width = 1348
		ixtalRegion.height = 1348
		ixtalRegion.visible = false

		// Shurima Icon
		const shurimaTexture = await Assets.load("icons/shurima.png")
		const shurimaHoverTexture = await Assets.load("hover-icons/shurima-hover.png")
		const shurimaIcon = vp.addChild(new Sprite(shurimaTexture))
		shurimaIcon.x = 910
		shurimaIcon.y = 630
		shurimaIcon.zIndex = 10
		shurimaIcon.height = 70
		shurimaIcon.width = 70
		shurimaIcon.roundPixels = true
		shurimaIcon.label = "shurima"

		// Shurima Text
		const shurimaText = new Text({
			text: "Shurima",
			style: {
				fontFamily: "Cinzel",
				fontSize: 26,
				fill: "#FFFFDE",
				stroke: {
					color: "#000000", // Black outline
					width: 2.5,
				},
				align: "center",
			},
		})
		shurimaText.x = 900
		shurimaText.y = 685
		vp.addChild(shurimaText)

		// Shurima Terrain
		const shurimaTerrain = await Assets.load("region-terrain/shurima.png")
		const shurimaRegion = vp.addChild(new Sprite(shurimaTerrain))
		shurimaRegion.x = 219
		shurimaRegion.y = -235
		shurimaRegion.width = 1348
		shurimaRegion.height = 1348
		shurimaRegion.visible = false

		// Targon Icon
		const targonTexture = await Assets.load("icons/targon.png")
		const targonHoverTexture = await Assets.load("hover-icons/targon-hover.png")
		const targonIcon = vp.addChild(new Sprite(targonTexture))
		targonIcon.x = 710
		targonIcon.y = 650
		targonIcon.zIndex = 10
		targonIcon.height = 70
		targonIcon.width = 70
		targonIcon.roundPixels = true
		targonIcon.label = "targon"

		// Targon Text
		const targonText = new Text({
			text: "Targon",
			style: {
				fontFamily: "Cinzel",
				fontSize: 26,
				fill: "#FFFFDE",
				stroke: {
					color: "#000000", // Black outline
					width: 2.5,
				},
				align: "center",
			},
		})
		targonText.x = 705
		targonText.y = 705
		vp.addChild(targonText)

		// Targon Terrain
		const targonTerrain = await Assets.load("region-terrain/targon.png")
		const targonRegion = vp.addChild(new Sprite(targonTerrain))
		targonRegion.x = 219
		targonRegion.y = -235
		targonRegion.width = 1348
		targonRegion.height = 1348
		targonRegion.visible = false

		// Demacia Icon
		const demaciaTexture = await Assets.load("icons/demacia.png")
		const demaciaHoverTexture = await Assets.load("hover-icons/demacia-hover.png")
		const demaciaIcon = vp.addChild(new Sprite(demaciaTexture))
		demaciaIcon.x = 580
		demaciaIcon.y = 380
		demaciaIcon.zIndex = 10
		demaciaIcon.height = 70
		demaciaIcon.width = 70
		demaciaIcon.roundPixels = true
		demaciaIcon.label = "demacia"

		// Demacia Text
		const demaciaText = new Text({
			text: "Demacia",
			style: {
				fontFamily: "Cinzel",
				fontSize: 26,
				fill: "#FFFFDE",
				stroke: {
					color: "#000000", // Black outline
					width: 2.5,
				},
				align: "center",
			},
		})
		demaciaText.x = 570
		demaciaText.y = 430
		vp.addChild(demaciaText)

		// Demacia Terrain
		const demaciaTerrain = await Assets.load("region-terrain/demacia.png")
		const demaciaRegion = vp.addChild(new Sprite(demaciaTerrain))
		demaciaRegion.x = 219
		demaciaRegion.y = -235
		demaciaRegion.width = 1348
		demaciaRegion.height = 1348
		demaciaRegion.visible = false

		vp.on("pointermove", (event) => {
			const screen = event.global
			const worldPoint = vp.toWorld(screen.x, screen.y)
			const hoveredChildren = vp.children.find((child) => {
				return (
					["freljord", "noxus", "ionia", "bilgewater", "shadow_isles", "piltover_zaun", "ixtal", "shurima", "targon", "demacia"].includes(
						child.label
					) &&
					child.x <= worldPoint.x &&
					worldPoint.x <= child.x + child.width &&
					child.y <= worldPoint.y &&
					worldPoint.y <= child.y + child.height
				)
			})
			if (hoveredChildren) {
				switch (hoveredChildren.label) {
					case "freljord":
						freljordIcon.texture = freljordHoverTexture
						freljordRegion.visible = true
						break
					case "noxus":
						noxusIcon.texture = noxusHoverTexture
						noxusRegion.visible = true
						break
					case "ionia":
						ioniaIcon.texture = ioniaHoverTexture
						ioniaRegion.visible = true
						break
					case "bilgewater":
						bilgewaterIcon.texture = bilgewaterHoverTexture
						bilgewaterRegion.visible = true
						break
					case "shadow_isles":
						shadowIslesIcon.texture = shadowIslesHoverTexture
						shadowIslesRegion.visible = true
						break
					case "piltover_zaun":
						piltoverZaunIcon.texture = piltoverZaunHoverTexture
						break
					case "ixtal":
						ixtalIcon.texture = ixtalHoverTexture
						ixtalRegion.visible = true
						break
					case "shurima":
						shurimaIcon.texture = shurimaHoverTexture
						shurimaRegion.visible = true
						break
					case "targon":
						targonIcon.texture = targonHoverTexture
						targonRegion.visible = true
						break
					case "demacia":
						demaciaIcon.texture = demaciaHoverTexture
						demaciaRegion.visible = true
						break
				}
			} else {
				freljordIcon.texture = freljordTexture
				freljordRegion.visible = false
				noxusIcon.texture = noxusTexture
				noxusRegion.visible = false
				ioniaIcon.texture = ioniaTexture
				ioniaRegion.visible = false
				bilgewaterIcon.texture = bilgewaterTexture
				bilgewaterRegion.visible = false
				shadowIslesIcon.texture = shadowIslesTexture
				shadowIslesRegion.visible = false
				piltoverZaunIcon.texture = piltoverZaunTexture
				ixtalIcon.texture = ixtalTexture
				ixtalRegion.visible = false
				shurimaIcon.texture = shurimaTexture
				shurimaRegion.visible = false
				targonIcon.texture = targonTexture
				targonRegion.visible = false
				demaciaIcon.texture = demaciaTexture
				demaciaRegion.visible = false
			}
		})

		//Moves into region page when region icon pressed
		vp.on("pointerdown", (event) => {
			const screen = event.global
			const worldPoint = vp.toWorld(screen.x, screen.y)
			const clickedChildren = vp.children.find((child) => {
				return (
					["freljord", "noxus", "ionia", "bilgewater", "shadow_isles", "piltover_zaun", "ixtal", "shurima", "targon", "demacia"].includes(
						child.label
					) &&
					child.x <= worldPoint.x &&
					worldPoint.x <= child.x + child.width &&
					child.y <= worldPoint.y &&
					worldPoint.y <= child.y + child.height
				)
			})
			if (clickedChildren) {
				switch (clickedChildren.label) {
					case "freljord":
						changeModalEmit("change_modal", "FRELJORD")
						freljordRegion.visible = true
						break
					case "noxus":
						changeModalEmit("change_modal", "NOXUS")

						break
					case "ionia":
						changeModalEmit("change_modal", "IONIA")

						break
					case "bilgewater":
						changeModalEmit("change_modal", "BILGEWATER")
						break
					case "shadow_isles":
						changeModalEmit("change_modal", "SHADOW_ISLES")
						break
					case "piltover_zaun":
						changeModalEmit("change_modal", "PILTOVER_ZAUN")
						break
					case "ixtal":
						changeModalEmit("change_modal", "IXTAL")
						break
					case "shurima":
						changeModalEmit("change_modal", "SHURIMA")
						break
					case "targon":
						changeModalEmit("change_modal", "TARGON")
						break
					case "demacia":
						changeModalEmit("change_modal", "DEMACIA")
						break
				}
			}
		})
	}

	const hover = ref()

	onMounted(() => {
		const hover = new Audio("soundfiles/sfx/regionhover.mp3")
		hover.loop = true
		hover.volume = 0.5
	})

	onBeforeUnmount(() => {
		if (hover.value) {
			hover.value.pause()
			hover.value.currentTime = 0
		}
	})

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
