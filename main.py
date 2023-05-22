import sys
import shutil

from game import *
from clips import *
from scrape import *
from download import *
from createVideo import *
from upload import *
from thumbnail import *
from utils import *


game = sys.argv[1]
timeGap = sys.argv[2]
iteration = sys.argv[3]
outFolderName = f"{game} {timeGap}{iteration}"

def init(game, timeGap, iteration):

    try:
        gameId = getGameId(stringToUrl(game))
        print("Fetching Clips")
        rawJsonClipData = getClips(gameId, parseTimeGap(timeGap))
        print("Done Fetching")
        print("Parsing JSON")
        parsedClipData = parseClips(rawJsonClipData)
        print("Finished Parsing")
        print("Fetching download links")
        videoLinkArr = getVideos(parsedClipData, "single") 
        print("Done Fetching")
        print("Initiating Download")
        clipsWithPath = downloadClips(videoLinkArr)
        print(clipsWithPath)
        print("Finished downloading clips")
        print("Creating Video")
        concat(clipsWithPath, outFolderName)
        print("Video Done!")
        print("Generating video details")
        generateVideoDetails(videoLinkArr, game, timeGap, iteration, outFolderName)
        print("Video details in details.txt")
        print("Generating Thumbnail")
        generateThumbnail(game, timeGap, iteration, outFolderName)
        print(f"Output is located in /complete/{outFolderName}")
        print("Removing Clips")
        deleteClips()
        print("Clips removed.")

    except:
        raise Exception("Failed")

init(game, timeGap, iteration)