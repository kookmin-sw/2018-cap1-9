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

m1 = [[1, 4, 1, 1,2], [4, 3, 3, 3,2], [3, 4, 2, 1,2], [4, 1, 3, 4,2], [2, 3, 2, 1,2],[2,2,2,2,2]]
m2 = [[3, 4, 4, 3, 1, 4, 4, 3, 2,2], [4, 2, 1, 4, 3, 4, 3, 3, 2,2], [3, 3, 2,	2, 4, 4, 2,	3, 1,2],
      [1, 1, 3, 2, 4,	3,	3,	1, 1,2], [2,	3, 4, 3, 2,	4,	2,	2, 3,2],[2,2,2,2,2,2,2,2,2,2]]


def summ2(list1, list2):
    a = list1[0]
    b = list1[1]
    a1 = list2[0]
    b1 = list2[1]
    return m1[a1][a] + m2[b1][b]

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
    elif (color == "grey"):
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

chooseCloth = input("어떤 옷을 선택하시겠습니까? : ")
l1 = [[1, 6], [2, 5], [0, 3], [3, 7]]
l2 = [[0, 3], [0, 4], [1, 4], [3, 4], [4, 3], [2, 2]]

select = l1[chooseCloth]
list3 = []
'''
topList = {}
pantsList = {}

for i in rows[0]:
    if(i[0] <= 9):
        topList[i[0]] = [changeColorUp(i[1]),i[4]]
'''
if(chooseCloth < =9):
    for i in l2:
        sum1 = summ2(select, i)
        list3.append(sum1)
else:
    for i in l1:
        sum1 = summ2(select, i)
        list3.append(sum1)

print(list3)