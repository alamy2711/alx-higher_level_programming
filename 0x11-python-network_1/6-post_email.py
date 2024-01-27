#!/usr/bin/python3
"""
Module: 6-post_email.py

Description:
This script takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the header of the response.

Usage: ./6-post_email.py <URL>
"""
import sys
import urllib.request

if __name__ == "__main__":
    url_link = sys.argv[1]

    request = urllib.request.Request(url_link)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
