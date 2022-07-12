#!/usr/bin/python3



import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as body:
            s = body.read()
            print(s.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
