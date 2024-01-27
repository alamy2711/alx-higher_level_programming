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
        with request.urlopen("https://intranet.hbtn.io/status") as res:
            res = res.read()
            print("Body res:")
            print("\t- type: {}".format(type(res)))
            print("\t- content: {}".format(res))
            print("\t- utf8 content: {}".format(res.decode(encoding='utf-8')))
