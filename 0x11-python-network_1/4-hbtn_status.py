#!/usr/bin/python3
""" fver """
import requests


if __name__ == "__main__":
    c = requests.get('https://alx-intranet.hbtn.io/status')
    x = c.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(x), x))
