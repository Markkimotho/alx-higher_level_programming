#!/usr/bin/python3

"""Module for fetching urls using urllib"""

import urllib.request

if __name__ =='__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        url_content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(url_content)))
    print("\t- content: {}".format(url_content))
    print("\t- uf8 content: {}".format(str(url_content)[2:-1]))
