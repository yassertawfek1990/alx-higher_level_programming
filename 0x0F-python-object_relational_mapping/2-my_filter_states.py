#!/usr/bin/python3
""" tsusa """
import MySQLdb
import sys


if __name__ == "__main__":
    zx = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cr = zx.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
               .format(sys.argv[4]))
    r = cr.fetchall()
    for x in r:
        print(x)
    cr.close()
    zx.close()
