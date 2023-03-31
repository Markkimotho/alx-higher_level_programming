#!/usr/bin/python3
"""Display response body
"""

import requests
import sys

if __name__ == '__main__':

    url = sys.argv[1]

    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except:
        print('Error code: {}'.format(r.status_code))
