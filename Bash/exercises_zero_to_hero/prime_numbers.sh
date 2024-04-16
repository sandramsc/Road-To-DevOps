#!/bin/bash
#########################
# Author: Sandra Ashipala
# Date: April 12, 2024
# Check if a number is a prime nukmber or not
# Version: v1
#########################


echo "Enter a number:"
read num

i=2

if [ $num -lt 2 ]
then
	echo "$num is not a prime numeber" # 2 is the smallest prime number
	exit
fi;

while [ $i -lt $num ]
do
	if [ `expr $num % $i` -eq 0 ]
	then 
		echo "$num is not a prime number" # there are other numbers that can divide into it
		exit
	fi;
	i=`expr $i + 1`
done

echo "$num is a prime number!"
