#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="34.225.233.100",
                     user="root",
                     passwd="1234",
                     db="VT")
cur = db.cursor()

cur.execute("SELECT * FROM Clothes_Info")

for row in cur.fetchall():
    print(row)

db.close()
