#!/usr/bin/python

import sys, os, subprocess
from xml.dom.minidom import parseString

HOST = "192.168.1.9"

def getsize():
    command = ("wget -q 'http://"+HOST+"/parsedit.php?immediate&WOI_WIDTH&WOI_HEIGHT' -O size.xml")
    subprocess.call(command, shell=True)


def readsize(name):
    try:
        file = open(name)
        data = file.read()
        file.close()
        dom = parseString(data)
        x = dom.getElementsByTagName("WOI_WIDTH")[0].childNodes[0]
        xxx = int(x.nodeValue)
        y = dom.getElementsByTagName("WOI_HEIGHT")[0].childNodes[0]
        yyy = int(y.nodeValue)
        print("----------------------------------camera values : ", xxx, yyy)
        command = ("rm size.xml")
        subprocess.call(command, shell=True)
        return xxx, yyy
        
    except IOError:
        pass


def launchgst(xxx,yyy):
    command = ('''gst-launch-0.10 rtspsrc location=rtsp://192.168.1.9:554 latency=100 ! rtpjpegdepay ! jpegdec ! queue ! jp462bayer ! "video/x-raw-bayer, width='''+str(xxx)+''', height='''+str(yyy)+''', format=grbg" ! queue ! bayer2rgb2 method=1 ! ffmpegcolorspace ! queue ! xvimagesink''')
    subprocess.call(command, shell=True)


def main():
    getsize()
    while True:
        factor = 2
        getsize()
        xxx, yyy = readsize("size.xml")
        launchgst(xxx/factor,yyy/factor)
       
main()
