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
    api_key = fc.GET_KEY("lol.txt")
    URL = f"{default_URL}/lol/summoner/v4/summoners/by-name/{summoner_name}"
    Header = Headers(api_key[0])
    res = requests.get(url=URL,headers=Header)
    if int(res.status_code) == 200:
        summoner = res.json()
        return summoner['id']
    else:
        return None

def get_auth_value(summoner_id):
    api_key = fc.GET_KEY("lol.txt")
    URL = f"{default_URL}/lol/platform/v4/third-party-code/by-summoner/{summoner_id}"
    Header = Headers(api_key[0])
    res = requests.get(url=URL,headers=Header)
    if int (res.status_code) == 200:
        summoner = res.json()
        return summoner


def get_summoner_tier(summoner_id):
    api_key = fc.GET_KEY("lol.txt")
    URL = f"{default_URL}/lol/league/v4/entries/by-summoner/{summoner_id}"
    Header = Headers(api_key[0])
    summoner_res = requests.get(url=URL,headers=Header)
    summoner_leagues = summoner_res.json()
    print(summoner_leagues)
    summoner_league = None
    for league in summoner_leagues:
        if league['queueType'] == "RANKED_SOLO_5x5":
            summoner_league = league
            break
        
    if summoner_league['queueType'] == 'RANKED_SOLO_5x5':
        solo_tier = summoner_league['tier']
        solo_rank = summoner_league['rank']
        return solo_tier,solo_rank
    else:
        return None,None