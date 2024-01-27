#!/usr/bin/python3
"""
Module: 7-error_code.py

Description:
This script takes in a URL, sends a request to the URL, and displays
the body of the response.

Usage: ./7-error_code.py <URL>
"""
import sys
import requests

if __name__ == "__main__":
    url_link = sys.argv[1]

    req = requests.get(url_link)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
