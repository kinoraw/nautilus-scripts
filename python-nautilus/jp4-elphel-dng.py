#!/usr/bin/python

'''
lanzar el script escribiendo esta linea dentro de la carpeta con los jp4s

ls *.jpg | parallel -j 8 python3 jp4-elphel-dng.py {}

ls jp4/*.jpg | parallel -j 8 python3 jp4-elphel-dng.py {}

'''

import os, sys, subprocess

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    command = "elphel_dng 100 "+f+e+" "+f+".dng"
    #print(command)
    subprocess.call(command,shell=True) 

    command = "exiftool -tagsFromFile "+f+e+" "+f+".dng" 
    print(command)
    subprocess.call(command,shell=True)   

    command = "exiftool -ISO=100 -FocalLength=4.5 -ExposureTime=0.04 -ApertureValue=2.0 -overwrite_original "+f+".dng"
    print(command)
    subprocess.call(command,shell=True) 

    #command = "dcraw -T -4 -q 3 -a "+f+".dng"
    command = "dcraw -T -4 -q 1 -a "+f+".dng"
    print(command)
    subprocess.call(command,shell=True)

    command = "rm "+f+".dng_original"
    print(command)
    subprocess.call(command,shell=True)

    command = "exiftool -tagsFromFile "+f+".dng"+" "+f+".tiff" 
    print(command)
    subprocess.call(command,shell=True)

    command = "rm "+f+".tiff_original"
    print(command)
    subprocess.call(command,shell=True)

    


