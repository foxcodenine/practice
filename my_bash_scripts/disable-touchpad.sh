#!/bin/bash
#
# Purpose: Toggle synaptic touchpad on/off
# Author: Fazle Arefin
# Reference: http://ubuntuforums.org/showthread.php?t=1536305
#

TOUCHPADID=`xinput | grep 'Touchpad' | cut -d '=' -f 2 | cut -c 1-2`    # this is touchpad id

SYNSTATE=$(xinput list-props "$TOUCHPADID" | grep "Device Enabled" | grep -Eo '.$')
if [ $SYNSTATE = 0 ]; then 
    xinput set-prop "$TOUCHPADID" "Device Enabled" 1
else 
    xinput set-prop "$TOUCHPADID" "Device Enabled" 0
fi

