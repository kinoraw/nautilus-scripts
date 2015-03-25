#!/bin/sh

for param in $@
  do
    echo $param
    if [ -f "$param" ]; then
	  base=${param%.*}
	  #By default the CRF value can be from 4–63, 
	  #and 10 is a good starting point.
	  #Lower values mean better quality. 
	  ffmpeg -i $param -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis $base-1Mbxsec_crf10.webm
  	fi	
done


