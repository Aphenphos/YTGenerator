def parseTimeGap(timeGap):
    validGaps = {
        "Daily": 1,
        "Weekly": 7,
        "Monthly": 30,
        "Yearly": 365
    }
    gapToDays = validGaps[timeGap]
    return gapToDays


def deleteClips():
    import shutil
    shutil.rmtree("./clips", ignore_errors=True)
    