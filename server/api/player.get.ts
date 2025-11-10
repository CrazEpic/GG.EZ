import { readFileSync } from "node:fs"
import { S3Client, GetObjectCommand } from "@aws-sdk/client-s3"
import { SQSClient, SendMessageCommand } from "@aws-sdk/client-sqs"

export default defineEventHandler(async (event) => {
	// read mock data from local file
	// const data = readFileSync("mock_stats.json", "utf-8")
	// const jsonData = JSON.parse(data)
	// return jsonData

	const query = getQuery(event)
	const gameName = encodeURIComponent(query.gameName as string)
	const tagLine = encodeURIComponent(query.tagLine as string)
	const region = query.region as string
	if (!gameName || !tagLine || (region != "americas" && region != "asia" && region != "europe")) {
		throw createError({ statusCode: 400, statusMessage: "Missing gameName or tagLine parameter. Region should also be americas, asia, or europe" })
	}

	const { RIOT_API_KEY, AWS_REGION, S3_SQS_ACCESS_KEY, S3_SQS_SECRET_ACCESS_KEY, SQS_QUEUE_URL } = useRuntimeConfig()

	if (!RIOT_API_KEY) {
		throw createError({ statusCode: 500, statusMessage: "Missing Riot API key" })
	}

	let puuid = undefined
	try {
		const riot_account = await $fetch(`https://${region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/${gameName}/${tagLine}`, {
			headers: {
				"X-Riot-Token": RIOT_API_KEY,
			},
		})
		if (!riot_account || !riot_account.puuid) {
			throw createError({ statusCode: 404, statusMessage: `Riot account not found ${region} ${gameName}#${tagLine}` })
		}
		puuid = riot_account.puuid
	} catch (error) {
		throw createError({ statusCode: 500, statusMessage: `Riot account not found ${region} ${gameName}#${tagLine}` })
	}

	const bucket_name = "ggez-rift-rewind"
	const s3_client = new S3Client({ region: AWS_REGION, credentials: { accessKeyId: S3_SQS_ACCESS_KEY, secretAccessKey: S3_SQS_SECRET_ACCESS_KEY } })

	let objectContent = undefined
	try {
		const command = new GetObjectCommand({ Bucket: bucket_name, Key: `players/${puuid}/info.json` })
		const response = await s3_client.send(command)
		objectContent = await response.Body.transformToString()
	} catch (error) {
		// not found in S3, continue to SQS step
		// start the sqs pipeline by sending message to sqs
		const sqs_client = new SQSClient({ region: AWS_REGION, credentials: { accessKeyId: S3_SQS_ACCESS_KEY, secretAccessKey: S3_SQS_SECRET_ACCESS_KEY } })
		const sqs_command = new SendMessageCommand({
			QueueUrl: SQS_QUEUE_URL,
			MessageBody: JSON.stringify({
				routing: region,
				puuid: puuid,
				gameName: gameName,
				tagLine: tagLine,
			}),
			MessageGroupId: "player",
		})
		try {
			await sqs_client.send(sqs_command)
		} catch (error) {
            console.log(error)
			throw createError({ statusCode: 500, statusMessage: `Failed to enqueue player data processing for ${gameName}#${tagLine}` })
		}
		return { puuid: puuid, statusMessage: "Player data processing has started.", content: "" }
	}

	if (objectContent) {
		// found in S3, so either in progress or completed
		try {
			// check the final stage of pipeline, the llm responses
			// const command = new GetObjectCommand({ Bucket: bucket_name, Key: `application/${puuid}/llm_responses.json` })
			// const response = await s3_client.send(command)
			// const llmStats = await response.Body.transformToString()

			const command_2 = new GetObjectCommand({ Bucket: bucket_name, Key: `application/${puuid}/application_stats.json` })
			const response_2 = await s3_client.send(command_2)
			const applicationStats = await response_2.Body.transformToString()
			return {
				puuid: puuid,
				statusMessage: "Player data retrieval complete.",
				content: {
					// llmStats: JSON.parse(llmStats),
					applicationStats: JSON.parse(applicationStats),
				},
			}
		} catch (error) {
			return { puuid: puuid, statusMessage: "Player data is still being processed.", content: "" }
		}
	}
})
