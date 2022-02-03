import os
import requests
import json


def GenUrl(steamid):
    baseurl = os.environ['apiurl']
    url = baseurl + steamid
    return url



def GetKills(steamid):
    url = GenUrl(steamid)
    response = requests.get(url)
    kills = response.json()["playerstats"]["stats"][0]["value"]
    return kills

