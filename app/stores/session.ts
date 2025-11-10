export const useSessionStore = defineStore("session", () => {
	const displaySR = ref(true)

	const freljordCardSR = ref<string | null>(null)
	const noxusCardSR = ref<string | null>(null)
	const shadowIslesCardSR = ref<string | null>(null)
	const bilgewaterCardSR = ref<string | null>(null)
	const ixtalCardSR = ref<string | null>(null)
	const shurimaCardSR = ref<string | null>(null)
	
	const freljordCardAram = ref<string | null>(null)
	const noxusCardAram = ref<string | null>(null)
	const shadowIslesCardAram = ref<string | null>(null)
	const bilgewaterCardAram = ref<string | null>(null)
	//    const ixtalCardAram = ref<string | null>(null)
	//    const shurimaCardAram = ref<string | null>(null)

	const visitedRegions = ref({
		freljord: false,
		noxus: false,
		ionia: false,
		shadowIsles: false,
		bilgewater: false,
		piltover_zaun: false,
		ixtal: false,
		shurima: false,
		targon: false,
		demacia: false,
	})

	return {
		displaySR,
		freljordCardSR,
		noxusCardSR,
		shadowIslesCardSR,
		bilgewaterCardSR,
		ixtalCardSR,
		shurimaCardSR,

		freljordCardAram,
		noxusCardAram,
		shadowIslesCardAram,
		bilgewaterCardAram,

		visitedRegions,
	}
})
