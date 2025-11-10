export default defineEventHandler(async (event) => {
	const query = getQuery(event)
	const puuid = encodeURIComponent(query.puuid as string)
	const championId = encodeURIComponent(query.championId as number)
	if (!puuid || !championId) {
		throw createError({ statusCode: 400, statusMessage: "Missing puuid, championId, or region parameter." })
	}

	const { RIOT_API_KEY } = useRuntimeConfig()

	if (!RIOT_API_KEY) {
		throw createError({ statusCode: 500, statusMessage: "Missing Riot API key" })
	}

	// TOO LATE TO GET THE REGIONS NOW
	const regions = ["EUN1", "EUW1", "KR", "NA1"]
	for (const region of regions) {
		try {
			const mastery = await fetch(`https://${region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/${puuid}/by-champion/${championId}`, {
				headers: {
					"X-Riot-Token": RIOT_API_KEY
				}
			})
			if (mastery && mastery.status === 200) {
				return mastery.json()
			}
		} catch (error) {
			// continue to next region
			await new Promise(r => setTimeout(r, 1000)); // wait 1 second between requests to avoid rate limiting
		}
	}
	throw createError({ statusCode: 404, statusMessage: `Champion mastery not found for puuid ${puuid} and championId ${championId}` })
})
