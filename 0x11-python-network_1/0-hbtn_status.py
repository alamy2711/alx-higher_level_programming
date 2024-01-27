#!/usr/bin/python3
"""
Module: 0-hbtn_status.py

Description:
This script fetches https://intranet.hbtn.io/status and prints
information about the response.
"""

from urllib import request


def fetch_hbtn_status():
    """
    Fetches https://intranet.hbtn.io/status and prints response information.
    """
    if __name__ == "__main__":
        url = "https://intranet.hbtn.io/status"
        with request.urlopen(url) as response:
            content = response.read()
            utf8_content = content.decode(encoding='utf-8')

            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(utf8_content))
