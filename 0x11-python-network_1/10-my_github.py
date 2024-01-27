#!/usr/bin/python3
"""
A script that:
- Takes your GitHub credentials (username and password)
as command-line arguments.
- Uses the GitHub API to display your user ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    authen = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=authen)
    print(req.json().get("id"))
