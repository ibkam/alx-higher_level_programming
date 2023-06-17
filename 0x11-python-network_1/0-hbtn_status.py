#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
	with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
		response = response.read()
		print("Body response:")
		print("\t - type: {}".format(type(response)))
		print("\t - content: {}".format(response))
		print("\t - utf content: {}".format(response.decode(encoding= 'utf-8')))
