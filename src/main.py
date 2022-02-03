import os
import requests
import json

class apiGetter:
    def __init__(self, steamid):
        self.steamid = steamid

    def GetKills(me):
        baseurl = os.environ['apiurl']
        url = baseurl + me.steamid
        response = requests.get(url)
        kills = response.json()["playerstats"]["steamID"]
        return kills

user = apiGetter("76561198396571874")

print(user.GetKills)