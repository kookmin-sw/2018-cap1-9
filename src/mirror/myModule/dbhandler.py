import MySQLdb as db

def connection(HOST, PORT, USER, PASSWORD, DB):
    try:
        conn = db.Connection(host=HOST, port=PORT,
                user=USER, passwd=PASSWORD, db=DB)
        cur = conn.cursor()
    except Exception as e:
        print(e)
    return conn, cur

def updateUpper(conn, cursor, dict):
    print("Inside update upper", end="")
    print(dict)
    cursor.execute("""
        UPDATE Coordinate
        SET x=%s, y=%s, width=%s, height=%s
        WHERE position='upper'
    """, (dict['x'], dict['y'], dict['w'], dict['h']))
    conn.commit()
    return 'update upper column done'

def updateLower(conn, cursor, dict):
    cursor.execute("""
        UPDATE Coordinate
        SET x=%s, y=%s, width=%s, height=%s
        WHERE position='lower'
    """, (dict['x'], dict['y'], dict['w'], dict['h']))
    conn.commit()
    return 'update lower column done'

def selectAll(cursor):
    cursor.execute("""SELECT * from Coordinate""")
    result = cursor.fetchall()

    ret = []
    for item in result:
        ret += item
    return ret

def selectUpper(cursor):
    sql = """
            SELECT * FROM
            Coordinate WHERE position='upper'
          """
    cursor.execute(sql)
    result = cursor.fetchall()

    ret = []
    for item in result:
        ret += item
    return ret

def selectLower(cursor):
    sql = """
            SELECT * FROM
            Coordinate WHERE position='lower'
          """
    cursor.execute(sql)
    result = cursor.fetchall()

    ret = []
    for item in result:
        ret += item
    return ret

def insertUpper(cursor, table, dict):
    cursor.execute ("""
        INSERT INTO Coordinate(x,y,width,height,position)
        VALUES(%s,%s,%s,%s,'upper')
    """, (dict[x], dict[y], dict[w], dict[h]))

def insertLower(cursor, table, dict):
    cursor.execute ("""
        INSERT INTO Coordinate(x,y,width,height,position)
        VALUES(%s,%s,%s,%s,'lower')
    """, (dict[x], dict[y], dict[w], dict[h]))

def delete():
    cursor.execute()
