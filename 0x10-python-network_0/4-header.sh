#!/bin/bash
# takes in URL as argument, sends GET request to URL, & displays body of response, A header variable X-School-User-Id must be sent with value 98
curl -s "$1" -H "X-School-User-Id: 98"
