#!/bin/bash

if [ "$1" = "" ];then
	wdir=${NAUTILUS_SCRIPT_CURRENT_URI#file://}
	wdir=${wdir//%20/ }
else
	filetype=$(file "$1")
	filetype=${filetype##*: }

	if [ "$filetype" = "directory" ];then
		wdir=${NAUTILUS_SCRIPT_SELECTED_FILE_PATHS%%$1*}
		wdir=$wdir/$1
	else
		wdir=${NAUTILUS_SCRIPT_SELECTED_FILE_PATHS%%$1*}
	fi
fi

cd $wdir
ls *.ply | parallel -j 8 sh /home/carlos/.local/share/nautilus/scripts/nautilus-scripts/MESHLAB/poisson9_full_res.sh {}
mkdir poisson9
mv *-poisson9.ply poisson9/ 

zenity --info --text="Listo :)"

