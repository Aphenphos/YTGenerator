import urllib.request
import os
import requests
def downloadClips(dlArr):
    if not os.path.exists("clips"):
        os.mkdir("clips")
    count = 0
    clipInfo = []
    for url in dlArr:
        print(f"Downloading clip {count}")
        resp = requests.get(url["downloadLink"], stream=True)
        with open(f"clips/{count}{url['streamerName']}.mp4", "wb+") as f:
            for chunk in resp.iter_content(chunk_size=1024):
                if chunk: f.write(chunk)
        info = {
            "clipPath": f"clips/{count}{url['streamerName']}.mp4",
            "streamerName": url['streamerName']
        }
        print(f"Finished Downloading Clip {count}")
        clipInfo.append(info)
        count += 1 
    return clipInfo
