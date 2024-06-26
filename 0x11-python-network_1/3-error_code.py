#!/usr/bin/python3
# python script that takes in a URL,
# sends a request to the URL and displays the body of the response
# (decoded in utf-8)
"""
    send a request to the URL & display body of the response
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
