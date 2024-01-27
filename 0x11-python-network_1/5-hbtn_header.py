#!/usr/bin/python3
"""
Module: 5-hbtn_header.py

Description:
This script sends a GET request to a given URL and displays the value of
the X-Request-Id header variable.

Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests

if __name__ == "__main__":
    url_link = sys.argv[1]

    req = requests.get(url_link)
    print(req.headers.get("X-Request-Id"))
