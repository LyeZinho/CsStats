import os
import requests
import json

class apiGetter:
    def __init__(me, steamid):
        me.steamid = steamid

    def GetKills(steamid):
        baseurl = os.environ['apiurl']
        url = baseurl + steamid
        response = requests.get(url)
        kills = response.json()["playerstats"]["stats"][0]["value"]
        return kills