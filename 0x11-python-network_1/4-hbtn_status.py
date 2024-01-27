#!/usr/bin/python3
"""
Module: fetch_hbtn_status.py

Description:
This script fetches https://intranet.hbtn.io/status using the requests library
and prints information about the response.

Requirements:
Install requests library using: pip install requests
"""

import requests


# Send a GET request to the specified URL
if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(req.text)}")
    print(f"\t- content: {req.text}")
