#!/usr/bin/python

import os, sys
import Image

"""
pythonic way to magic:
for root, dirs, files in os.walk('.'):
for f in files:
print os.path.splitext(os.path.join(root,f))
"""

import Image

im = Image.open("mono.jpg")
im.seek(1) # skip to the second frame

try:
    while 1:
        im.seek(im.tell()+1)
        # do something to im
except EOFError:
    pass # end of sequence



class ImageSequence:
    def __init__(self, im):
        self.im = im
    def __getitem__(self, ix):
        try:
            if ix:
                self.im.seek(ix)
            return self.im
        except EOFError:
            raise IndexError # end of sequence

for frame in ImageSequence(im):
    # ...do something to frame...
		
	#create a directory to send diferent frames
	filename = "./frame_diference/filename.txt"
	dir = os.path.dirname(filename)
	if not os.path.exists(dir):
		os.makedirs(dir)
	f, e = os.path.splitext(infile)
	outfile = "./frame_diference/z_" + infile + ".jpg"
	if infile != outfile:
		try:
			Image.open(infile).save(outfile)
		except IOError:
			print "cannot convert", infile

"""
for infile in sys.argv[1:]:

	#create a directory to send diferent frames
	filename = "./frame_diference/filename.txt"
	dir = os.path.dirname(filename)
	if not os.path.exists(dir):
		os.makedirs(dir)
	f, e = os.path.splitext(infile)
	outfile = "./frame_diference/z_" + infile + ".jpg"
	if infile != outfile:
		try:
			Image.open(infile).save(outfile)
		except IOError:
			print "cannot convert", infile

"""

