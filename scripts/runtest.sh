#!/bin/bash

# Run tests
if [ -z ${RESMONAUTHENV+x} ]; then
    source ./resmon-autoclient.env
fi

python3.6 -m unittest discover -p "*Test.py"
exit $?
