#!/bin/bash
# A script that sends a POST request with the content of a JSON file passed as a second argument to a URL passed as the first argument, and displays the body of the response.
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
