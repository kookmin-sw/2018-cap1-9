import sys
sys.path.append("myModule")
import threading
import simplejson
import DetectBody
import json
import dbhandler as db
import subprocess


HOST = "34.225.233.100"
PORT = 3306
USER = "root"
PASSWORD = "1234"
DB = "VT"
table = 'Coordinate'

coordi = {}
def get():
    while(True):
        output = subprocess.check_output(['tail', '-n 10', 'test.log'], universal_newlines=True)
        jsonList = output.split('\n')
        print("jsonList start")
        print(jsonList)
        print("josnList end")
        ret = {}
        for jsonLine in jsonList:
            print("josnLine: ", end="")
            print(jsonLine)
            try:
                temp = json.loads(jsonLine)
            except ValueError:
                print('error')
                continue
            if not (not temp['upper'] or not temp['lower']):
                ret = temp
                break
        print(ret)
        return ret

thread_u = threading.Thread(target=DetectBody.findBody())
thread_u.start()

try:
    conn, cur = db.connection(HOST, PORT, USER, PASSWORD, DB)
except Exception as e:
    print(e)

    coordi = get()

try:
    for upper in coordi['upper']:
        print(db.updateUpper(conn, cur, upper))
    for lower in coordi['lower']:
        print(db.updateLower(conn, cur, lower))
except KeyError:
    print("KeyError")
