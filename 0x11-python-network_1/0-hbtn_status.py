#!/usr/bin/python3

"""Module showing url status
using urllib
"""
import urllib.request

if __name__ == "__main__":
    url_request = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    # make the request and get the response
    with urllib.request.urlopen(url_request) as response:
        # read the reponse using the .read attribute of the response object
        url_content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(url_content)))
    print("\t- content: {}".format(url_content))
    print("\t- uf8 content: {}".format(str(url_content)[2:-1]))
