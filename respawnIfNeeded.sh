#!/bin/bash

if ! daemon --name=day --running && ! daemon --name=night --running; then
	daemon --name=day -- raspistill -mm average -ISO 100 -n -rot 180 -w 640 -h 480 -v -drc high -t 0 -ts -o /var/ramdisk/pic%d.jpg --latest /var/ramdisk/pic.jpg -a 12
	echo Starting day
	exit 
fi
if (! ~/mengivakt/isNighttime.py) && daemon --name=night --running; then
	daemon --name=night --stop
	sleep 1
	daemon --name=day -- raspistill -mm average -ISO 100 -n -rot 180 -w 640 -h 480 -v -drc high -t 0 -ts -o /var/ramdisk/pic%d.jpg --latest /var/ramdisk/pic.jpg -a 12
	echo Stopping night starting day
	exit
fi

if ~/mengivakt/isNighttime.py && daemon --name=day --running; then
	daemon --name=day --stop
	sleep 1
	daemon --name=night -- raspistill -ev 4 -awb off -awbg 1.0,2.2 -ex verylong -mm average -ISO 16000 -ss 80000000 -n -rot 180 -w 640 -h 480 -v -drc high -t 0 -ts -o /var/ramdisk/pic%d.jpg --latest /var/ramdisk/pic.jpg -a 12
	echo Stopping day starting night
	exit
fi
echo Nothing to do
