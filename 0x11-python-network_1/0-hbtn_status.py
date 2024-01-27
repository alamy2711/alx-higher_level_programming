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
    url = "https://intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode(encoding='utf-8')

        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {utf8_content}")


if __name__ == "__main__":
    fetch_hbtn_status()
