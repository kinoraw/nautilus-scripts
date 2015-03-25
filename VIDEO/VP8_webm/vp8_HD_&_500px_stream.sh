#!/bin/sh

for param in $@
  do
    echo $param
    if [ -f "$param" ]; then
	  base=${param%.*}
	  ffmpeg -i $param -c:v libvpx -minrate 3M -maxrate 3M -b:v 3M -c:a libvorbis $base-HD.webm 
	  ffmpeg -i $param -c:v libvpx -vf scale=500:-1 -minrate 1M -maxrate 1M -b:v 1M -c:a libvorbis $base-500px.webm
  	fi	
done


