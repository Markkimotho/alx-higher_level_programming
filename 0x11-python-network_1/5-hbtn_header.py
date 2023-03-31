#!/usr/bin/python3

"""module that provides a response header value
of a url using requests package
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    id_content = response.headers['X-Request-Id']
    print(id_content)
