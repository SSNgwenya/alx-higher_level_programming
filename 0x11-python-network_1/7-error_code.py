#!/usr/bin/python3
"""
Script that sends a request to a URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, prints the error code.
"""
import requests
from sys import argv

def main():
    """
    Sends a GET request to the URL provided as a command-line argument,
    prints the body of the response if the status code is less than 400,
    or prints the error code if the status code is 400 or higher.
    """
    url = argv[1]  # Get the URL from the command-line argument
    response = requests.get(url)  # Send a GET request to the URL

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)  # Print the body of the response

if __name__ == "__main__":
    main()

