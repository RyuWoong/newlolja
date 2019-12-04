import requests
import os
import log
import myfunction as fc

# app = Flask(__name__)
default_URL = "https://kr.api.riotgames.com"

def Headers(api_key):
    return {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": api_key,
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }

def get_summoner_id(summoner_name):
    api_key = fc.GET_KEY("lolapi.txt")
    URL = f"{default_URL}/lol/summoner/v4/summoners/by-name/{summoner_name}"
    Header = Headers(api_key)
    res = requests.get(url=URL,headers=Header)
    if int(res.status_code) == 200:
        summoner = res.json()
        return summoner['id']


def get_summoner_tear(member_lol):
    api_key = fc.GET_KEY("lolapi.txt")
    URL = f"{default_URL}/lol/summoner/v4/summoners/by-name/{member_lol}"
    Header = Headers(api_key)
    res = requests.get(url=URL,headers=Header)
    if int(res.status_code) == 200:
        summoner = res.json()
        summoner_id = summoner['id']
        URL = f"{default_URL}/lol/league/v4/entries/by-summoner/{summoner_id}"
        summoner_res = requests.get(url=URL,headers=Header)
        summoner_leagues = summoner_res.json()
        summoner_league = None
        for league in summoner_leagues:
            if league['queueType'] == "RANKED_SOLO_5x5":
                summoner_league = league
            else:
                pass
        if summoner_league == None:
            return None, None
        elif summoner_league['queueType'] == 'RANKED_SOLO_5x5':
            solo_tier = summoner_league['tier']
            solo_rank = summoner_league['rank']
            return solo_tier,solo_rank
        else:
            return None,None
    else:
        log.logger.error(f"@@LOL API ERROR | No Summoner target : {member_lol}")
        return None,None