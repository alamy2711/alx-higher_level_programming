#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
"""

import sys
import requests

if __name__ == "__main__":

    # Construct the URL for the GitHub API based on
    # provided username and repository
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    # Send a GET request to retrieve commit information from the GitHub API
    req = requests.get(url)
    com = req.json()

    try:
        # Iterate through the 10 most recent commits and print relevant
        # information
        for i in range(10):
            print("{}: {}".format(
                com[i].get("sha"),
                com[i].get("commit").get("author").get("name")))
    except IndexError:
        # Handle the case where there are fewer than 10 commits
        pass
