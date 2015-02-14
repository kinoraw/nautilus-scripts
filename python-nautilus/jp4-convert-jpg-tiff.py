#!/usr/bin/python

'''
lanzar el script escribiendo esta linea dentro de la carpeta con los jp4s

ls *.jpg | parallel -j 8 python3 jp4-convert-jpg-tiff.py {}

ls jp4/*.jpg | parallel -j 8 python3 jp4-convert-jpg-tiff.py {}

empieza a las 3:20 de la mañana...
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

    command = "exiftool -ISO=100 -FocalLength=4.5 -ApertureValue=2.0 -overwrite_original "+f+".dng"
    print(command)
    subprocess.call(command,shell=True) 

    command = "dcraw -T -4 -q 3 -a "+f+".dng"
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

    print(f)
    name = (f+"_mantiuk.jpg")
    print("-----------------------",name)

    command = "pfsin "+f+".dng | pfstmo_mantiuk06 -f 0.1 -s 0.8 | pfsgamma --gamma 3.5 | pfsout "+ name
    print(command)
    subprocess.call(command,shell=True)
    
    name = (f+"_fattal.jpg")
    command = "pfsin "+f+".dng | pfstmo_fattal02 | pfsgamma --gamma 2.6 | pfsout "+ name
    print(command)
    subprocess.call(command,shell=True)


