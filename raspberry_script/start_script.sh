#!/bin/sh

process=$(netstat -nlp | grep 9999 | wc -l)
if [ $process = 0 ]; then
	cd /home/pi/raspberry_script/pep
	java -jar pep.jar 9999 &
	sleep 30
	
	cd ..
	python light_attribute_manager.py &
	python publish_script.py &
fi;
