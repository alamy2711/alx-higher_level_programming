#!/usr/bin/python3
"""
Module: 2-post_email.py

Description:
This script takes in a URL, sends a POST request to the passed
URL with an email parameter, and displays the body of the response.

Usage: ./2-post_email.py <URL> <email>
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url_link = sys.argv[1]
    valeur = {"email": sys.argv[2]}
    donne = urllib.parse.urlencode(valeur).encode("ascii")

    request = urllib.request.Request(url_link, donne)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
