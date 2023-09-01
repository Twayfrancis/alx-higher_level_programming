#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()

        print('Body response:')
        print('- type:', type(body))
        print('- content:', repr(body))
        print('- utf8 content:', body.decode('utf-8'))
