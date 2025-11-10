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
		public: {},
		RIOT_API_KEY: "",
		AWS_REGION: "",
		S3_SQS_ACCESS_KEY: "",
		S3_SQS_SECRET_ACCESS_KEY: "",
		SQS_QUEUE_URL: "",
	},
})
