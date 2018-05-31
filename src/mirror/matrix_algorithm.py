import pymysql.cursors
import sys
import time


selectClotheNo = 0

m1 = [[1, 4, 1, 1, 2], [4, 3, 3, 3, 2], [3, 4, 2, 1, 2], [4, 1, 3, 4, 2], [2, 3, 2, 1, 2], [2, 2, 2, 2, 2]]
m2 = [[3, 4, 4, 3, 1, 4, 4, 3, 2, 2], [4, 2, 1, 4, 3, 4, 3, 3, 2, 2], [3, 3, 2, 2, 4, 4, 2, 3, 1, 2],
      [1, 1, 3, 2, 4, 3, 3, 1, 1, 2], [2, 3, 4, 3, 2, 4, 2, 2, 3, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

while(True):
    db = pymysql.connect(host="34.225.233.100",
                         user="root",
                         passwd="1234",
                         db="VT",
                         port=3306)

    curs1 = db.cursor()
    curs2 = db.cursor()
    curs3 = db.cursor()
    curs4 = db.cursor()
    sql1 = "select * from Clothes_Info"
    sql2 = "select * from Coordinate"
    sql3 = "select * from Recommend_List"
    sql3_1 = "UPDATE Recommend_List SET addr = %s WHERE No=1"
    sql3_2 = "UPDATE Recommend_List SET addr = %s WHERE No=2"
    sql3_3 = "UPDATE Recommend_List SET addr = %s WHERE No=3"


    curs1.execute(sql1)
    curs2.execute(sql2)
    curs3.execute(sql3)
    rows = curs1.fetchall()
    selectClothe = curs2.fetchall()
    position = curs3.fetchall()


    if(selectClotheNo == selectClothe[0][5] and selectClotheNo == selectClothe[1][5]):
        continue

    def summ2(list1, list2):
        a = list1[1]
        b = list1[2]
        a1 = list2[1]
        b1 = list2[2]
        return m2[a1][a] + m1[b1][b]

    def changeColorUp(color):
        if(color == "Green"):
            return 0
        elif(color == "Blue" or color == 'Right-Blue'):
            return 1
        elif (color == "Yellow"):
            return 2
        elif (color == "Pink"):
            return 3
        elif (color == "Navy"):
            return 4
        elif (color == "White"):
            return 5
        elif (color == "Black" or color =='black'):
            return 6
        elif (color == "Grey" or color == "darkgray" or color == "darkslategray" or color =="dimgrey" or color == "silver"):
            return 7
        else:
            return 9

    def changeKindUp(Kind):
        if (Kind == "Blouse"):
            return 0
        elif (Kind == "T-Shrit"):
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
        elif (color == "Khaki" or color == "Charcoal"):
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
        elif (Kind == "Mini-Skirt"):
            return 4
        else:
            return 5
    isuplow = 0
    chooseCloth = 0
    if(position[0][1] == 'null' or position[0][1] == 'null'):
        continue
    if(position[0][1] == "upper"):
        chooseCloth = selectClothe[1][5]
        isuplow = 1
    elif(position[0][1] == "lower"):
        chooseCloth = selectClothe[0][5]
        isuplow = 0

    if (selectClothe[0][5] == 'black' and selectClothe[1][5] == 'black'):
        curs4.execute(sql3_1, 'black')
        curs4.execute(sql3_2, 'black')
        curs4.execute(sql3_3, 'black')
        db.commit()
        continue

    list3 = []

    topList = []
    pantsList = []

    for i in rows:
        if(i[4] == "upper"):
            list1 = [i[0], changeColorUp(i[1]), changeKindUp(i[2]), i[3]]
            topList.append(list1)
        else:
            list1 = [i[0], changeColorDown(i[1]), changeKindDown(i[2]), i[3]]
            pantsList.append(list1)
    j = 0
    if(chooseCloth != 'black'):
        select = int(chooseCloth)
    if(isuplow == 1):
        k=0
        for i in topList:
            if(i[3] == chooseCloth):
                select = i[0]
                break
            k += 1
        for i in pantsList:
            sum1 = summ2(topList[k], i)
            pantsList[j].append(sum1)
            j += 1
        newlist = sorted(pantsList, key=lambda x:x[4],reverse=True)
    else:
        k = 0
        for i in pantsList:
            if(i[3] == chooseCloth):
                select = i[0]
                break
            k += 1
        for i in topList:
            sum1 = summ2(i, pantsList[k])
            topList[j].append(sum1)
            j += 1
        newlist = sorted(topList,  key=lambda x: x[4],reverse=True)
    one = newlist[0][3]
    two = newlist[1][3]
    thr = newlist[2][3]

    curs3.execute(sql3_1, one)
    curs3.execute(sql3_2, two)
    curs3.execute(sql3_3, thr)

    a = curs3.fetchall()

    db.commit()