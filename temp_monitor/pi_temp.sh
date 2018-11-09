#!/bin/bash

while true
do 
 temp=$(/opt/vc/bin/vcgencmd measure_temp)
 echo "Rasp Pi Temp : $temp"
 sleep 1
done
