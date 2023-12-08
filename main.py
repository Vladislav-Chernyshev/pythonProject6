from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/Николай/')
def nike():
    return 'Привет, Николай!'
