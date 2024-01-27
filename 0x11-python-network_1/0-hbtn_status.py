#!/usr/bin/python3
"""
Module: 0-hbtn_status.py

Description:
This script fetches https://intranet.hbtn.io/status and prints
information about the response.
"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
