import pymysql

db = pymysql.connect(host="34.225.233.100",
                     user="root",
                     passwd="1234",
                     db="VT",
                     port = 3306)

curs = db.cursor()

sql = "select * from Clothes_Info"
curs.execute(sql)

rows = curs.fetchall()
print(rows[0][2])
for i in rows:
    print(i)

m1 = [[1, 4, 1, 1], [4, 3, 3, 3], [3, 4, 2, 1], [4, 1, 3, 4], [2, 3, 2, 1]]
m2 = [[3, 4, 4, 3, 1, 4, 4, 3, 2], [4, 2, 1, 4, 3, 4, 3, 3, 2], [3, 3, 2,	2, 4, 4, 2,	3, 1],
      [1, 1, 3, 2, 4,	3,	3,	1, 1], [2,	3, 4, 3, 2,	4,	2,	2, 3]]


def summ2(list1, list2):
    a = list1[0]
    b = list1[1]
    a1 = list2[0]
    b1 = list2[1]
    return m1[a1][a] + m2[b1][b]


l1 = [[1, 6], [2, 5], [0, 3], [3, 7]]
l2 = [[0, 3], [0, 4], [1, 4], [3, 4], [4, 3], [2, 2]]

select = l1[0]
list3 = []
for i in l2:
    sum1 = summ2(select, i)
    list3.append(sum1)

print(list3)
