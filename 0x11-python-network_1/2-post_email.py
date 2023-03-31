#!/usr/bin/python3

""" module that POSTs an email to the url
and displays the body using the urllib
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    email = urllib.parse.urlencode(email)
    email = email.encode('utf-8')

    url_request = urllib.request.Request(url, email)

    with urllib.request.urlopen(url_request) as response:
        content = response.read()
        content = content.decode('utf-8')
        print(content)
