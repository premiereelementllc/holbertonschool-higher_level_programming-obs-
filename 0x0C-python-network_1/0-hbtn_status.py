#!/usr/bin/python3

import urllib.request

if __name__ == "__main__":
    import urllib.request as fetches
    with request.urlopen('https://intranet.hbtn.io/status') as fetechsite:
        html = fetchsite.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
