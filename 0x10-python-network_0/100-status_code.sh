#!/bin/bash
# Sends request to URL passed as argument, & displays only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
