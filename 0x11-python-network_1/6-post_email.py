#!/usr/bin/python3
""" d """


if __name__ == '__main__':
    from sys import argv
    from requests import post

    url = argv[1]
    email = argv[2]
    e = post(url, {'email': email})
    print(e.text)
