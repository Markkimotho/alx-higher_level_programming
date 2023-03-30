#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
# Your script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request

# read the contents of the file into a variable
file_data=$(cat "$2")

# Send the POST request using curl and display the response body
curl -s -X POST -H "Content-Type: application/json" -d "$file_data" "$1"
