!#/bin/bash
############################
# Author: Sandra Ashipala
# Date: April 9, 2024
#
# This script outputs the node health
#
# Version: v1
############################

set -x # set -x prints output in debug mode / prints the command that you are using, this method is better than writing echo statments i.e echo "Prints the CPU details"

set -e # exit script when there is an error

set -o pipefail

df -h

free -g

nproc

ps -ef | grep amazon | awk -F " " '{print $2}'

