#!/usr/bin/python3
"""all states from hbtn_0e_0_usa"""

import MySQLdb

def _state():
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306,  user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id ASC")
    inrows = curs.fetchall()

    for row in inrows:
        print(row)
    curs.close()
    db.close()

if __name__ == "__main__":
    _state()
