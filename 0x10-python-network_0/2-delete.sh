#!/bin/bash
# sends DELETE request to URL passed as 1st argument & displays body of response
curl -sX DELETE "$1"
