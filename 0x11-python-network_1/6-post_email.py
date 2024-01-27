#!/usr/bin/python3
"""
Module: 6-post_email.py

Description:
This script takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the header of the response.

Usage: ./6-post_email.py <URL>
"""
import sys
import requests

if __name__ == '__main__':
    url_link = sys.argv[1]
    email = sys.argv[2]
    req = requests.post(url_link, data={'email': email})
    print(req.text)
