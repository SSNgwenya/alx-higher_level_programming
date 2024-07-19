#!/bin/bash
# Send JSON POST request to URL passed as 1st argument, & displays body of response.
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
