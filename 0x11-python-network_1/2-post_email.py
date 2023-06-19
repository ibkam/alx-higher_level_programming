#!/usr/bin/python3

"""sending a post request with the url and an email"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
    print(body)
