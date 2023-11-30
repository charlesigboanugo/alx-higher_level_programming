#!/bin/bash
# Make a request to the server using curl
curl -s -X PUT 0.0.0.0:5000/catch_me -L -d "user_id=98" -H "Origin: HolbertonSchool"
