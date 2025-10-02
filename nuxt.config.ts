import tailwindcss from "@tailwindcss/vite"

export default defineNuxtConfig({
	compatibilityDate: "2025-07-15",
	devtools: { enabled: true },
	css: ["~/assets/css/main.css"],
	vite: {
		plugins: [tailwindcss()],
	},
	modules: ["@pinia/nuxt"],
	runtimeConfig: {
		RIOT_API_KEY: process.env.NUXT_RIOT_API_KEY || "missing",
		public: {},
	},
})