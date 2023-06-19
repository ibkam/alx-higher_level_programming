#!/usr/bin/python3
"""
 takes in a URL, sends a request to the URL and displays
 the value of the variable X-Request-Id in the response header
"""
import requests
from sys import agrv

if __name__ == "__main__":
    url = sys.agrv[1]
    
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
