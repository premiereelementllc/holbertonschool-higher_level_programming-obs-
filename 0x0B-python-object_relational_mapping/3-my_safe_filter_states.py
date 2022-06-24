#!/usr/bin/python3

""" display  all values in the  states table  from  hbtn_0e_0_usa database"""


if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE BINARY name = %s", (argv[4], ))
    inrows= curs.fetchall()

    for row in inrows:
            print(row)

    curs.close()
    db.close()
