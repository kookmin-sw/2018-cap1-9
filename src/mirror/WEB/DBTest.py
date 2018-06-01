import pymysql
import sys


db = pymysql.connect(host="34.225.233.100",
                     user="root",
                     passwd="1234",
                     db="VT",
                     port = 3306)


curs2 = db.cursor()
sql2= "select * from Coordinate"
curs2.execute(sql2)
selectClothe = curs2.fetchall()

isuplow = 0
chooseCloth = 0
if(selectClothe[0][5] == None or selectClothe[0][5] == "black"):
    chooseCloth = selectClothe[1][5]
    isuplow = 1
    print("Lower selected")
else:
    chooseCloth = selectClothe[0][5]
    isuplow = 0
    print("Upper selected")
