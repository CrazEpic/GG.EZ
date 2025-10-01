import os
import requests
from development.riot_models import LeagueEntryDTO, AccountDTO, SummonerDTO, MatchDTO
from typing import List, Optional, Literal


RIOT_API_KEY = os.getenv("RIOT_API_KEY")

america_server = "https://americas.api.riotgames.com"
na_server = "https://na1.api.riotgames.com"
esports_server = "https://esports.api.riotgames.com"


def send_riot_api_request(base_url, path, query_params=None):
    return requests.get(
        base_url + path + (query_params if query_params else ""), headers={"X-Riot-Token": RIOT_API_KEY}
    )


def get_summoner_by_puuid(encrypted_puuid: str) -> Optional[SummonerDTO]:
    response = send_riot_api_request(base_url=na_server, path=f"/lol/summoner/v4/summoners/by-puuid/{encrypted_puuid}")
    if response.status_code == 200:
        return SummonerDTO(**response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


def get_league_entries_by_puuid(encrypted_puuid: str) -> List[LeagueEntryDTO]:
    response = send_riot_api_request(base_url=na_server, path=f"/lol/league/v4/entries/by-puuid/{encrypted_puuid}")
    if response.status_code == 200:
        data = response.json()
        return [LeagueEntryDTO(**entry) for entry in data]
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []


def get_league_entries_by_ranked_queue_tier_division(
    queue: Literal["RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TT", "RANKED_TFT"],
    tier: Literal[
        "CHALLENGER",
        "GRANDMASTER",
        "MASTER",
        "DIAMOND",
        "PLATINUM",
        "GOLD",
        "SILVER",
        "BRONZE",
        "IRON",
    ],
    division: Literal["I", "II", "III", "IV"],
    page: int = 1,
) -> List[LeagueEntryDTO]:
    response = send_riot_api_request(
        base_url=na_server,
        path=f"/lol/league/v4/entries/{queue}/{tier}/{division}",
        query_params=f"?page={page}",
    )
    if response.status_code == 200:
        data = response.json()
        return [LeagueEntryDTO(**entry) for entry in data]
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []


def get_match_by_id(match_id: str) -> Optional[MatchDTO]:
    response = send_riot_api_request(base_url=america_server, path=f"/lol/match/v5/matches/{match_id}")
    if response.status_code == 200:
        return MatchDTO(**response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


def get_matches_by_puuid(
    puuid: str,
    startTime: Optional[int],
    endTime: Optional[int],
    queue: Optional[int],
    type: Literal["ranked", "normal", "tourney", "tutorial"],
    start=0,
    count=20,
) -> List[str]:
    response = send_riot_api_request(
        base_url=america_server,
        path=f"/lol/match/v5/matches/by-puuid/{puuid}/ids",
        query_params=f"?start={start}&count={count}"
        + (f"&startTime={startTime}" if startTime else "")
        + (f"&endTime={endTime}" if endTime else "")
        + (f"&queue={queue}" if queue else "")
        + (f"&type={type}" if type else ""),
    )
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []


def get_account_by_puuid(puuid: str) -> AccountDTO:
    response = send_riot_api_request(base_url=america_server, path=f"/riot/account/v1/accounts/by-puuid/{puuid}")
    if response.status_code == 200:
        data = response.json()
        return AccountDTO(**data)
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []


def get_account_by_game_name_and_tag_line(game_name: str, tag_line: str) -> AccountDTO:
    response = send_riot_api_request(
        base_url=america_server, path=f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    )
    if response.status_code == 200:
        data = response.json()
        return AccountDTO(**data)
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []
