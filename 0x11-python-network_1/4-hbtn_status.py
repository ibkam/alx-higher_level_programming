#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    request = urlib.request.get('https://alx-intranet.hbtn.io/status')
    print("Body response:$")
    print("\t- type: {}".format(type(read.text)))
    print("\t- content: {}".format(type(read.text)))
