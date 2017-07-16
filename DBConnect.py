# -*- coding: utf-8 -*-
import MySQLdb

connection = MySQLdb.connect(db = "j14002",user = "J14002")
cursor = connection.cursor()


cursor.execute("select * from users")
result = cursor.fetchall()

for row in result:
    print row[0]

cursor.close()
connection.close()

