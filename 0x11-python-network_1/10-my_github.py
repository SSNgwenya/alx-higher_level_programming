#!/usr/bin/python3
"""
Module to access the GitHub API and use the information
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

def main():
    """
    Script that takes GitHub credentials (username and password) and
    uses the GitHub API to display the user id.
    """
    if len(argv) != 3:
        print("Usage: ./script.py <username> <personal_access_token>")
        return

    user = argv[1]
    password = argv[2]
    
    try:
        response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(user, password))
        response.raise_for_status()  # Raises an HTTPError for bad responses
        profile_info = response.json()
        print(profile_info['id'])
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError:
        print("Invalid JSON response")
    except KeyError:
        print("Key 'id' not found in response")

if __name__ == "__main__":
    main()

