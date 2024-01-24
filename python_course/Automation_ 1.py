'''
download videos from you tube using the python pytube library.
imports and modules
'''
# -> * means everything
import sys
from sys import argv 
# import pytube
from pytube import YouTube
link = argv[0]
yt = YouTube(link)
print("song title", yt.title)
print("song views", yt.views, end=(" "))

youtube_download = yt.stream.get_highest_resolution()
youtube_download.download("c:/Users/ALMAGUFULI/Desktop/PYTHON PROGRAMMING/")
#https://youtu.be/hXPgfdxFIlg?si=4vrrshNZGB_iWCjq
print (yt)