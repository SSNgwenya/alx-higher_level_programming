#!/bin/bash
# takes in URL, sends request to URL,& displays size of body of response
curl -sI "$1" | awk '/Content-Length/{print $2}'
