#!/bin/sh

for param in $@
  do
    echo $param
    if [ -f "$param" ]; then
	  base=${param%.*}
	  # preset slow
	  # the audio stream of the input file is simply ​
	  # stream copied over to the output and not re-encoded. 
	  
	  # The range of the quantizer scale is 0-51: where 0 is lossless, 
	  # 23 is default, and 51 is worst possible. 
	  # A lower value is a higher quality and 
	  # a subjectively sane range is 18-28. 
	  # Consider 18 to be visually lossless or nearly so: 
	  # it should look the same or nearly the same as the input 
	  # but it isn't technically lossless.

      # The range is exponential, 
      # so increasing the CRF value +6 is roughly half the bitrate 
      # while -6 is roughly twice the bitrate. 
      # General usage is to choose the highest CRF value that 
      # still provides an acceptable quality. If the output looks good, 
      # then try a higher value and if it looks bad then choose a lower value. 
	  ffmpeg -i $param -c:v libx264 -preset slow -crf 22 -c:a copy $base-h264_CRF.mkv
  	fi	
done


