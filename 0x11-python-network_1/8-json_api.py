#!/usr/bin/python3
"""
A script that:
- Takes in a letter as a command-line argument.
- Sends a POST request to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    # Check if a letter is provided as a command-line argument
    letter_char = "" if len(sys.argv) == 1 else sys.argv[1]

    # Prepare payload for the POST request
    pay_load = {"q": letter_char}

    # Send a POST request to the specified URL
    req = requests.post("http://0.0.0.0:5000/search_user", data=pay_load)

    try:
        # Try to parse the response as JSON
        res = req.json()

        # Check if the response is empty
        if res == {}:
            print("No result")
        else:
            # Print the response in the specified format
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        # Handle the case where the response is not a valid JSON
        print("Not a valid JSON")
