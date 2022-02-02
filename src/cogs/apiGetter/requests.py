import requests
import json

class apiGetter:
    def __init__(me, steamid):
        me.steamid = steamid

    def ApiUrlGen(steamid):
        baseurl = ""
        endurl = baseurl + steamid
        return endurl

        
