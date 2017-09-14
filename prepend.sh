#!/bin/bash

filename=$2
cat $1 $2 >> tmp
rm $2
mv tmp $filename
