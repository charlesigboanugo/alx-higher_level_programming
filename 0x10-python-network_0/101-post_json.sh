#!/bin/bash

# Check if the required arguments are provided
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

url=$1
filename=$2

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "Error: File not found - $filename"
    exit 1
fi

# Send a JSON POST request with the file content in the body
curl -X POST -H "Content-Type: application/json" -d "@$filename" "$url"

