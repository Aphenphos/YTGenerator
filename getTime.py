import datetime
def getToday():
    unformattedNow = datetime.datetime.today().strftime("%Y-%m-%d")
    formattedNow = f"{unformattedNow}T00:00:00Z"
    return formattedNow

def getPastDate(timeGap): 
    unformattedYesterday = datetime.datetime.today() - datetime.timedelta(days=timeGap)
    yesterday = unformattedYesterday.strftime("%Y-%m-%d")
    formatted = f"{yesterday}T00:00:00Z"
    return formatted