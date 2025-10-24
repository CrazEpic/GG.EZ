module.exports = {
	apps: [
		{
			name: "Nuxt-Web-Server",
			port: "3000",
			// exec_mode: "cluster",
			// instances: "max",
			script: "./.output/server/index.mjs",
		},
        {
            name: "FastAPI-Backend",
            script: "./_prod.sh",
            interpreter: "bash",
            cwd: "./backend-fastapi"
        }
	],
}
