#!/usr/bin/python3

""" list all cities associated with a state in the hbtn_0e_4_usa database"""


if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    curs = db.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name FROM cities \
        LEFT JOIN states ON cities.state_id = states.id WHERE \
        states.name = \"{}\"".format(argv[4]))
    cities = curs.fetchall()
    cities = [city[1] for city in cities]
    print(", ".join(cities))

    curs.close()
    db.close()
