#!/usr/bin/python3
# python script that takes in a URL,
# sends a request to the URL and displays the body of the response
"""
    send a request to URL & display body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    rq = requests.get(url)
    if rq.status_code >= 400:
        print("Error code: {}".format(rq.status_code))
    else:
        print(rq.text)
