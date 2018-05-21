import sys
sys.path.append("myModule")
import threading 
from flask import Flask, request
from flask_mysqldb import MySQL
import simplejson
import MultiFind
import json
import dbhandler as db

app = Flask(__name__)

HOST = "34.225.233.100"
PORT = 3306
USER = "root"
PASSWORD = "1234"
DB = "VT"
table = 'Coordinate'

try:
    cur = db.connection(HOST, PORT, USER, PASSWORD, DB)
except Exception as e:
    print(e)


@app.route('/')
def main():
    thread_u = threading.Thread(target=MultiFind.findBody())
    thread_u.start()
    return 'Hello, '

@app.route('/thread-test')
def thread():
    return 'threading working'

@app.route('/get-coordinate')
def setCoordinate():
    with open('myModule/test2.log', 'r') as file:
        data = json.load(file)
    print(data)
    return json.dumps(data)

@app.route('/db-save')
def save():
    coor = {'lower': [{'w': 1000, 'h': 2134, 'x': 179, 'y': 6}], 'upper': [{'w': 25, 'h': 30, 'x': 179, 'y': 6}]}

    print(db.updateUpper(cur, coor['upper'][0]))
    print(db.updateLower(cur, coor['lower'][0]))
    ret = db.selectAll(cur)

    return json.dumps(ret)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
