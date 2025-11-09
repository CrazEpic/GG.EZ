import { readFileSync } from "node:fs"

export default defineEventHandler(async (event) => {
    // read mock data from local file
    const data = readFileSync("mock_stats.json", "utf-8")
    const jsonData = JSON.parse(data)
    return jsonData
})
