#!/bin/sh

for param in $@
  do
    echo $param
    if [ -f "$param" ]; then
	  base=${param%.*}
	  ffmpeg -i $param -c:v libvpx -b:v 1M -c:a libvorbis $base-1Mbxsec.webm
  	fi	
done


