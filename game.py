import requests
import json
from config import *
def getGameId(game):
    headers = {
        "Client-Id": client_id,
        "Authorization": f"Bearer {token}"
    }
    req = requests.get(f"https://api.twitch.tv/helix/games?name={game}", headers=headers)
    gameId = req.json()["data"][0]["id"]
    return gameId

def stringToUrl(name):
    return name.replace(" ", "+")
