#!/usr/bin/python3
"""
Module: 4-hbtn_status.py

Description:
This script fetches https://intranet.hbtn.io/status using the requests library
and prints information about the response.

Requirements:
Install requests library using: pip install requests
"""

import requests


# Send a GET request to the specified URL
if __name__ == '__main__':
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
