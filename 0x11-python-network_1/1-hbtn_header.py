#!/usr/bin/python3
"""script to send a request to the url and display the value
in the request_id"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
