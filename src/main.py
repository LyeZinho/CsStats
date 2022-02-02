from os import kill
from cogs.api.requests import apiGetter

user = apiGetter("76561198396571874")

kills = user.GetKills

print(kills)