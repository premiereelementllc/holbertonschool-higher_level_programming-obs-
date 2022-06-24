#!/usr/bin/python3

""" list all cities from  hbtn_0e_4_usa database"""


if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    curs = db.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states on cities.state_id = states.id ORDER BY cities.id ASC")
    inrows= curs.fetchall()

    for row in inrows:
            print(row)

    curs.close()
    db.close()
