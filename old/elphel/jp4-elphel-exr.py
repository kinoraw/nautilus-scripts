#!/usr/bin/python

'''

lanzar el script escribiendo esta linea dentro de la carpeta con los jp4s:

ls *.jpg | parallel -j 8 python jp4-elphel-exr.py {}

'''

import os, sys, subprocess

for infile in sys.argv[0:]:
    f, e = os.path.splitext(infile)
    command = "elphel_dng 100 "+f+e+" "+f+".dng"
    subprocess.call(command,shell=True) 

    command = "exiftool -tagsFromFile "+f+e+" "+f+".dng" 
    subprocess.call(command,shell=True)   

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
