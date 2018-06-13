#!/bin/bash

# Run tests
if [ -z ${RESMONAUTHENV+x} ]; then
    source ./resmon-autoclient.env
fi

MODULES=`find -wholename './test/*.py' | sed -e 's/\.\.//g' \
    | sed '/__init__/d'`
    
for VARIABLE in $MODULES
do
	echo $VARIABLE
	python3 $VARIABLE
done
