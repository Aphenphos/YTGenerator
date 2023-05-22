import time
import multiprocessing
from selenium import webdriver
from bs4 import BeautifulSoup

def getVideos(clipArr, mode):
    #ONLY USE MULTI MODE IF YOU HAVE A STRONG CPU/RAM AND INTERNET SPEED!
    clipDownloadLinks = []
    if mode == "multi":
      pool = multiprocessing.Pool()
      pool = multiprocessing.Pool(processes=len(clipArr))
      clipDownloadLinks = pool.map(getDLLink, clipArr)
    if mode == "single":
        for clip in clipArr:
            dlInfo = getDLLink(clip)
            if dlInfo != None:
                clipDownloadLinks.append(dlInfo)
    return clipDownloadLinks



#Add counter so you know clip gathering prog
def getDLLink(clipInfo):

        print(f"searching for {clipInfo}")
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get(clipInfo["clipURL"])
        time.sleep(1)
        html = driver.page_source
        bs = BeautifulSoup(html, "lxml")
        video = bs.find('video').get("src")
        if video == None:
             driver.close()
             return
        driver.close()
        print(video)
        return {
            "streamerName": clipInfo["streamerName"],
            "clipURL": clipInfo["clipURL"],
            "downloadLink":video ,
            "duration": clipInfo["duration"]
            }