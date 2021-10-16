#1016_ytdownloader

from pytube import YouTube

yt = YouTube("影片網址")

stream = yt.streams.first()

stream.download()

