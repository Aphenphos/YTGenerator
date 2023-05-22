import requests
from config import *
from getTime import * 

def getClips(gameId, timeGap):
    today = getToday()
    pastDate = getPastDate(timeGap)
    headers = {
        "Client-Id": client_id,
        "Authorization": f"Bearer {token}"
    }
    req = requests.get(f"https://api.twitch.tv/helix/clips?first=40&game_id={gameId}&started_at={pastDate}&ended_at={today}", headers=headers)

    return req.json()

def parseClips(clipsJson):
    parsedClips = []
    parsedClipsDuartion = 0
    desiredDuration = 900
    count = 0
    while parsedClipsDuartion < desiredDuration:
        clipData = {
            "streamerName": clipsJson["data"][count]["broadcaster_name"],
            "clipURL": clipsJson["data"][count]["url"],
            "duration": clipsJson["data"][count]["duration"]
        }
        parsedClips.append(clipData)
        parsedClipsDuartion += clipsJson["data"][count]["duration"]
        count += 1
    print(parsedClips)
    return parsedClips

