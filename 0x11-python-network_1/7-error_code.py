#!/usr/bin/python3
""" script that takes in a URL, sends a request to
 the URL and displays the body of the response."""

import sys
import requests

if __name__ == "__main__":
	url = sys.argv[1]
	request = requests.get(url)
	if requests.status_code >= 400:
		print("Error code: {}".format(requests.status_code))
	else:
		print(requests.text)
