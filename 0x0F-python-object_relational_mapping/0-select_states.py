#!/usr/bin/python3
"""  stsa ahbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    zx = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cr = zx.cursor()
    cr.execute("SELECT * FROM states")
    r = cr.fetchall()
    for x in r:
        print(x)
    cr.close()
    zx.close()
