#!/usr/bin/python

import os, sys
import Image, ImageChops

#get a list of files
list = ()
for root, dirs, files in os.walk('.'):
	for f in files:
		print os.path.splitext(os.path.join(root,f))
		list.append(f)

#create a directory to send diferent frames
filename = "./frame_diference/filename.txt"
dir = os.path.dirname(filename)
if not os.path.exists(dir):
	os.makedirs(dir)

image1 = Image.open(sys.argv[1])
image2 = Image.open(sys.argv[2])

ImageChops.subtract(image1, image2)

f, e = os.path.splitext(infile)
if infile != out:
	try:
		Image.open(infile).save(out)
	except IOError:
		print "cannot convert", infile

