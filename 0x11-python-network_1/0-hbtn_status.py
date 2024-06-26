#!/usr/bin/python3
# python script that fetches 'https://alu-intranet.hbtn.io/status'
"""
    fetch 'https://alx-intranet.hbtn.io/status'
"""
import urllib.request


if __name__ == "__main__":
    request = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
