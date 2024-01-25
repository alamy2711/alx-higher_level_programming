#!/bin/bash
# This script takes in a URL, sends a request to that URL
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
