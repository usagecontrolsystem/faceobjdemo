#!/bin/sh

#run the pep jar

cd /home/eitdigitaldemo/login_scripts

user=$(whoami)
if [ "$user" != "root" ]; then
	echo $(whoami) >> file.txt
	echo logged >> file.txt


	cd /home/antonio/login_scripts/pep
	process=$(netstat -nlp | grep 9999 | wc -l)
	if [ $process = 0 ]; then
		java -jar pep.jar 9999 &

		sleep 20
	fi;

	echo HELLO***************
	cd ..

	python3 /home/antonio/login_scripts/login.py --user $(whoami) &
fi;
