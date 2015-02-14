#!/usr/bin/python

'''

usage:

ls *.dng | parallel -j 8 python dng-elphel-exr.py {}

'''

import os, sys, subprocess

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    
    command = "exiftool -ISO=100 -FocalLength=4.5 -ExposureTime=0.04 -ApertureValue=2.0 -overwrite_original "+f+".dng"
    subprocess.call(command,shell=True) 
    
    # dcraw -T -4 -q 1 -a -m 2 
    # |
    # `-> you have to configure this inside qtpfsgui preferences

    command = "qtpfsgui "+f+".dng -s "+f+".exr"
    subprocess.call(command,shell=True)

    command = "rm "+f+".dng_original"
    subprocess.call(command,shell=True)

    command = "rm "+f+".dng"
    subprocess.call(command,shell=True)
