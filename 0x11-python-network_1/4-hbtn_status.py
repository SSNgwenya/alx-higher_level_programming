#!/usr/bin/python3
"""
Module using requests that fetches https://alx-intranet.hbtn.io/status
"""
import requests

def main():
    """
    Function that fetches https://alx-intranet.hbtn.io/status
    """
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    body = r.text

    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))

if __name__ == "__main__":
    main()

