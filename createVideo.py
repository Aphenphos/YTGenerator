from moviepy.editor import *
import os
def concat(clipPaths, folderName):
    clips = []
    fadeDuration = 1
    for clipPath in clipPaths:
        c = clipPath['clipPath']
        cObj = VideoFileClip(c, target_resolution=(1080, 1920))
        clips.append(cObj)
    clips = [clip.crossfadein(fadeDuration) for clip in clips]
    if not os.path.exists(f"./complete/{folderName}"):
        os.mkdir(f"./complete/{folderName}")
    out = concatenate_videoclips(clips, method="chain", padding=-fadeDuration)
    out.write_videofile(f"./complete/{folderName}/finished.mp4", fps=24, threads=8, codec="h264_nvenc", bitrate="8M")
    