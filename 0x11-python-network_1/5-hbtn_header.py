#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable
found in the response header.
"""
import requests
import sys

def main():
    """
    Function that sends a request to a URL and displays
    the value of the X-Request-Id variable in the response header.
    """
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))

if __name__ == "__main__":
    main()

