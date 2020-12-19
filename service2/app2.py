host='0.0.0.0'
port='5000'

from flask import Flask
import requests
import pprint

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return '''  <h1> Welcome  to GCLOUD APP :  <h1> '''

@app.route('/<int:number>/')
def incrementer(number):
    url_number = "http://localhost:3000/{}".format(number)
    result=requests.get(url_number)
    return result.text

@app.route('/<string:name>/')
def hello(name):
    url_name = "http://localhost:3000/{}".format(name)
    username = requests.get(url_name)
    return username.text

app.run(host,port)
