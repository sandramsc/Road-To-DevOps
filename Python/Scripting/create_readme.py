#!/usr/bin/python3

##############################
# Author: Sandra Ashipala
# Date: April, 10, 2024
# Version: v1
# This script is made to auto empty the recycle bin
##############################

import os
from github import Github

def create_readme(repo_path):
	with open(os.path.join(repo_path, "README.md"), "w") as readme_file:
		readme_file("# TEXT HERE")

def git_int(repo_path, github_token):
	# initialize a local git repo
	os.chdir(repo_path)
	os.system("git init")

	# Initialize a github repo
	g = Github(github_token)
	user = g.get_user()
	repo_name = os.path.basename(repo_path)
	print(f"Initialized '{repo_name}' repo on GitHub.")

def main():
	# Specify the folder path where the directory will be created
	folder_path = input("Enter the folder path where you want the repo to be created:")

	# Specify the github access token
	github_token = input("Enter you GitHub access token:")

	# If the folder does not already exist, create it
	os.makedirs(folder_path, exist_ok=True)

	# Initialize the repo
	git_init(folder_path, github_token)

	# Generate a README.md
	create_readme(folder_path)
	print("Successfully create a README.md file")

if __name__ == "__main__"
	main()
