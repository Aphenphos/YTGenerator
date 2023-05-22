import time
def generateVideoDetails(clipArr, game, timeGap, iteration, outFolder):
    streamersInTitle = generateTopStreamerTitle(clipArr)
    streamerList = generateDescriptionStreamerList(clipArr)

    title = f"Best of {game} {timeGap} ({streamersInTitle}) #{iteration} \n"

    videoTimeStamps = generateVideoTimeStamps(clipArr)
    description = f"{game} {timeGap} Highlights #{iteration} \n {streamerList} \n {videoTimeStamps}"

    tags = ["twitch", "highlights", {game}, {timeGap}, "gaming"]


    file = open(f"./complete/{outFolder}/info.txt", "w+", encoding="utf-8")
    file.write(f"title:{title}")
    file.write(f"description:{description}")
    file.write(f"tags:{tags}")
    file.close()

def generateTopStreamerTitle(clipArr):
    topStreamers = []
    i = 0
    while len(topStreamers) < 3:
        toAdd = clipArr[i]["streamerName"]
        topStreamers.append(toAdd)
        i += 1
        for x in enumerate(topStreamers):
            topStreamers = list(dict.fromkeys(topStreamers))
    string = ", "
    return (string.join(topStreamers))

def generateDescriptionStreamerList(clipArr):
    arrOfStreamers = []
    for streamer in clipArr:
        if streamer["streamerName"] not in arrOfStreamers:
            arrOfStreamers.append(streamer["streamerName"])
        else: continue
    stringified = ""
    for streamer in arrOfStreamers:
        stringified += f"{streamer}: https://www.twitch.tv/{streamer}\n"
    return stringified



def generateVideoTimeStamps(clipArr):
    timestampInSeconds = 0
    timeStamps = ""
    for clip in clipArr:
        timeStamps = timeStamps + f"{clip['streamerName']}: {time.strftime('%M:%S',time.gmtime(timestampInSeconds))} \n"
        timestampInSeconds += clip["duration"] - 1
    return timeStamps


