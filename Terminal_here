#!/bin/bash

#Open a terminal with the currentdir of nautilus as workdir.
#Don't need to select any file in the currentdir.
##########################################################################
#                        Nautilus "Terminal Here" Script                 #
##########################################################################
#                                                                        #
# Created by Xinyu Du                                                    #
# Emails: glacier_05@yahoo.com.cn                                        #
##########################################################################
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
gnome-terminal --working-directory="$wdir"
