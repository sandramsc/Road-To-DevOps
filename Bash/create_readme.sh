#!/usr/bin/python3

##############################
# Author: Sandra Ashipala
# Date: April, 10, 2024
# Version: v1
# This script is made to auto empty the recycle bin
##############################

import os
import subprocess

def create_template(repo_path):
    template = """
Some text here

    """
    readme_path = os.path.join(repo_path, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write(template)

        # Check if it is a new repo
        readme_path = os.path.join(repo_path, "README.md")
        if not os.path.exists(readme_path):
            create_readme(repo_path)

if __name__ = "__main__":
    main()
