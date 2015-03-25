#!/bin/sh

for param in $@
  do
    echo $param
    if [ -f "$param" ]; then
	  base=${param%.*}
	  # you can choose different values for the bitrate other than 1M, 
	  # e.g. 500K, but you must set all options (i.e., minrate, maxrate and b:v) to the same value. 
	  ffmpeg -i $param -c:v libvpx -minrate 3M -maxrate 3M -b:v 3M -c:a libvorbis $base-cbr_3Mxsec.webm

  	fi	
done


