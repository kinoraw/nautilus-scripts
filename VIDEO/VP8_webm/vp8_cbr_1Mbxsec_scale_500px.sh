#!/bin/sh

for param in $@
  do
    echo $param
    if [ -f "$param" ]; then
	  base=${param%.*}
	  # you can choose different values for the bitrate other than 1M, 
	  # e.g. 500K, but you must set all options (i.e., minrate, maxrate and b:v) to the same value. 
	  ffmpeg -i $param -c:v libvpx -vf scale=500:-1 -minrate 1M -maxrate 1M -b:v 1M -c:a libvorbis $base-cbr_1Mxsec_500px.webm

  	fi	
done


