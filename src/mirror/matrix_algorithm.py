import pymysql
import sys

db = pymysql.connect(host="34.225.233.100",
                     user="root",
                     passwd="1234",
                     db="VT",
                     port = 3306)

curs = db.cursor()

sql = "select * from Clothes_Info"
curs.execute(sql)

rows = curs.fetchall()

m1 = [[1, 4, 1, 1,2], [4, 3, 3, 3,2], [3, 4, 2, 1,2], [4, 1, 3, 4,2], [2, 3, 2, 1,2],[2,2,2,2,2]]
m2 = [[3, 4, 4, 3, 1, 4, 4, 3, 2,2], [4, 2, 1, 4, 3, 4, 3, 3, 2,2], [3, 3, 2,	2, 4, 4, 2,	3, 1,2],
      [1, 1, 3, 2, 4,	3,	3,	1, 1,2], [2,	3, 4, 3, 2,	4,	2,	2, 3,2],[2,2,2,2,2,2,2,2,2,2]]


def summ2(list1, list2):
    a = list1[1]
    b = list1[2]
    a1 = list2[1]
    b1 = list2[2]
    return m2[a1][a] + m1[b1][b]

def changeColorUp(color):
    if(color == "Green"):
        return 0
    elif(color == "Blue"):
        return 1
    elif (color == "Yellow"):
        return 2
    elif (color == "Pink"):
        return 3
    elif (color == "Navy"):
        return 4
    elif (color == "White"):
        return 5
    elif (color == "Black"):
        return 6
    elif (color == "Grey"):
        return 7
    else:
        return 9

def changeKindUp(Kind):
    if (Kind == "Blouse"):
        return 0
    elif (Kind == "Tshrit"):
        return 1
    elif (Kind == "Shrit"):
        return 2
    elif (Kind == "Suit"):
        return 3
    else:
        return 4

def changeColorDown(color):
    if(color == "Dark Blue"):
        return 0
    elif (color == "Light Blue"):
        return 1
    elif (color == "Beige"):
        return 2
    elif (color == "Khaki" | color == "Charcoal"):
        return 3
    elif (color == "Black"):
        return 4
    else:
        return 5

def changeKindDown(Kind):
    if (Kind == "Active Wear"):
        return 0
    elif (Kind == "Skirt"):
        return 1
    elif (Kind == "Jean"):
        return 2
    elif (Kind == "Suit"):
        return 3
    elif (Kind == "Mini Skirt"):
        return 4
    else:
        return 5

chooseCloth = int(sys.argv[1])

list3 = []

topList = []
pantsList = []

for i in rows:
    if(i[0] <= 9):
        list1 = [i[0], changeColorUp(i[1]), changeKindUp(i[4])]
        topList.append(list1)
    else:
        list1 = [i[0], changeColorDown(i[1]), changeKindDown(i[4])]
        pantsList.append(list1)
j = 0
select = int(chooseCloth)
if(int(chooseCloth) <= 9):
    for i in pantsList:
        sum1 = summ2(topList[select], i)
        pantsList[j].append(sum1)
        j += 1
    newlist = sorted(pantsList, key=lambda x:x[3],reverse=True)
else:
    for i in topList:
        sum1 = summ2(i, pantsList[select-10])
        topList[j].append(sum1)
        j += 1
    newlist = sorted(topList,  key=lambda x: x[3],reverse=True)
f = open("list.txt", 'w')
for i in newlist:
    if(i[3]>=5):
        f.write(i[0])