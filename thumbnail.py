from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def generateThumbnail(game, timeGap, iteration, folderName):
    topText = timeGap
    midText = f"{game} Highlights"
    botText = f"#{iteration}"
    height = 720
    width = 1280
    image = Image.open(f"./assets/{game}.png")
    font = ImageFont.truetype("/home/m/dev/twitch-scraper/assets/impact.ttf", 130)
    draw = ImageDraw.Draw(image)
    topBox = draw.textbbox((0,0), topText, font=font)
    midBox = draw.textbbox((0,0), midText, font=font)
    botBox = draw.textbbox((0,0), botText, font=font)
    draw.text((round((width - topBox[2]) / 2), 0), topText, font=font)
    draw.text((round((width - midBox[2]) / 2), round((height - midBox[3]) / 2)), midText, font=font)
    draw.text((round((width - botBox[2]) / 2), 550), botText, font=font)
    
    image.save(f"./complete/{folderName}/thumbnail.jpg")

