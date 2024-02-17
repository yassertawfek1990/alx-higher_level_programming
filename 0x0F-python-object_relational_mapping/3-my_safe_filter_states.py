#!/usr/bin/python3
"""  lists0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    zx = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cr = db.cursor()
    mch = sys.argv[4]
    cr.execute("SELECT * FROM states WHERE name LIKE %s", (mch, ))
    r = cr.fetchall()
    for x in r:
        print(x)
    cr.close()
    zx.close()
