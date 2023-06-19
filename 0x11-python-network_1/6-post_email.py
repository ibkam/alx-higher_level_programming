#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST"""
import sys
import requests

if __name__ == "__main__"
url = sys.agrv[1]
value = {"email:" sys.argv[2]}

request = requests.post(url, data=value)
print(request.text)
