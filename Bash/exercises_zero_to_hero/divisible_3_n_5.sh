#!/bin/bash

####################
# Author: Sandra Ashipala
# Date: April 12, 2024
# This script finds all numbers dicisible by 3 or 5 but not 15 i.e 3*5=15
# Version: v1
####################


# define a range
for i in {1..100}; do
# set the conditions
if ([ `expr $i % 3` == 0 ] || [ `expr $i % 5` == 0 ]) && [ `expr $i % 15` != 0 ];
then
	echo $i
fi;
done
