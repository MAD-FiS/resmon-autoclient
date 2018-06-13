#!/bin/bash

# Generates python documentation. Later it moves html files to docs dictionary
if [ -z ${RESMONAUTHENV+x} ]; then
    source ./resmon-autoclient.env
    echo "NOT"
fi

rm ./docs/* -f
pydoc3 -w $(pydoc3 -k src)
for f in ./*.html ; do mv "$f" ./docs/ ; done
