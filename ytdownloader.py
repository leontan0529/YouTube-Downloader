#Done by Lyon

#(Current) V1.1 as of 040222
# - Allow users to pick their desired file format
# - Allow users to rename file or allow file to be auto-named

#Import modules
from __future__ import unicode_literals
import youtube_dl

#YouTube Downloader Program
link = input("Enter the YouTube link that you would like to download: ")
ans = input("Do you want to download in video or audio format?")

meta = youtube_dl.YoutubeDL().extract_info(link, download=False)
def yt_mp3():
    name_choice = input("Do you want to name your file or allow auto-naming from link? (Y/N)")
    if name_choice.lower() == 'y':
        yt_name = input("Name: ")
        filename = "{}.mp3".format(yt_name)
    else:
        filename = f"{meta['title']}.mp3"
    ydl_opts={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print("Download complete!")

def yt_mp4():
    name_choice = input("Do you want to name your file or allow auto-naming from link? (Y/N)")
    if name_choice.lower() == 'y':
        yt_name = input("Name: ")
        filename = "{}.mp4".format(yt_name)
    else:
        filename = f"{meta['title']}.mp4"
    ydl_opts={
        'format':'bestvideo/best',
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print("Download complete!")

if ans.lower() == 'video':
    yt_mp4()
elif ans.lower() == 'audio':
    yt_mp3()
else:
    print("You did not insert a valid option. Goodbye!")
    exit()

