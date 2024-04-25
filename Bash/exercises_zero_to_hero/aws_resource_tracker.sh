#!/bin/bash

############################
# Author: Sandra Ashipala
# Data: 20.04.2024
#
# Version: v1
# This script will report the AWS resource usage
############################

set -x

# AWS S3
# AWS EC2
# AWS Lambda
# AWS IAM Users

# List S3 buckets
echo "Print list of s3 buckets"
aws s3 ls > resourceTracker

# List EC2 instances - read the docs to find the command
echo "Print list of ec2 buckets"
aws ec2 describe-instances | jq '.Reservations[].Instances[].InstanceId'

# List lambda
echo "Print list of lambda functions"
aws lambda list-functions > resourceTracker:q!

# List IAM users
echo "Print list of IAM users"
aws iam list-users
