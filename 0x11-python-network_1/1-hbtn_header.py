#!/usr/bin/python3

"""Module for response header value
using urllib
"""

import sys
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])

    # make the request and get the response
    with urllib.request.urlopen(req) as response:
        # get the value of the "X-Request-Id" header using
        # .headers attribute and .get method to get the value
        id_header = response.headers.get("X-Request-Id")
    print(id_header)
