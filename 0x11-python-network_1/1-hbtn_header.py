#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys

def main(url):
    """
    takes in URL, sends request to the URL,
    and displays the value of the X-Request-Id variable found in the header of the response.
    """
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: ./script_name.py <URL>")

