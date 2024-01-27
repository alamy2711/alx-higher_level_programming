#!/usr/bin/python3
"""
Module: 3-error_code.py

Description:
This script takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        # Send a request to the specified URL
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))

    except error.HTTPError as err:
        # Handle HTTP errors and display the error code
        print('Error code:', err.code)
