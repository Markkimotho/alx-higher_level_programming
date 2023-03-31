#!/usr/bin/python3

"""module for status of url
using requests package
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    data = requests.get(url)
    text_data = data.text
    print('Body response:')
    print('\t- type: {}'.format(type(text_data)))
    print('\t- content: {}'.format(text_data))
