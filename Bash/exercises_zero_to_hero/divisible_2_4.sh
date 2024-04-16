#!/bin/bash
###################
# Author: Sandra Ashipala
# Date: April 12,2024
# This script finds numbers divisible by 2 and 4 but not 4*2=8
# Version: v1
###################

for i in {1..100}; do
if ([ `expr $i % 2` == 0 ] || [ `expr $i % 4` == 0 ]) && [ `expr $i % 8` != 0 ];
then
	echo $i
fi;
done
