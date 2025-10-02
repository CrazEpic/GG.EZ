export default defineEventHandler(async (event) => {
	const { RIOT_API_KEY } = useRuntimeConfig(event)
	const query = getQuery(event)
	const gameName = query.gameName as string
	const tagLine = query.tagLine as string

	const response = await $fetch(`https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/${gameName}/${tagLine}`, {
		headers: {
			"X-Riot-Token": RIOT_API_KEY,
		},
	})

	return response
})
