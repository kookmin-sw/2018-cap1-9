import sys
sys.path.append("myModule")
from flask import Flask, request
import simplejson
import UpperBody
import LowerBody

app = Flask(__name__)

@app.route('/')
def main():
    UpperBody.findBody()
    LowerBody.findBody()
    return 'Hello, '
