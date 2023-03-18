#!/usr/bin/python3
"""0x0F. Python - Object-relational mapping - task 0. Get all states"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) != 4:
        sys.exit('Use: 0-select_states.py <mysql username> <mysql password>'
                 ' <database name>')

    conn = MySQLdb.connect(host='localhost', port=3306, user='root',
                           passwd='root', db='my_db', charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
