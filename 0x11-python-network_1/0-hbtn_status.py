#!/usr/bin/python3

"""Module showing url status
using urllib
"""
import urllib.request

if __name__ == "__main__":
    url_request = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    with urllib.request.urlopen(url_request) as response:
        url_content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(url_content)))
        print("\t- content: {}".format(url_content))
        print("\t- uf8 content: {}".format(url_content.decode("utf-8"))
