#!/usr/bin/python3

"""
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            content = content.decode('utf-8')
            print(content)

    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
