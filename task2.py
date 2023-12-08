from flask import Flask

app = Flask(__name__)


@app.route('/Федор/'.casefold())
@app.route('/Fedor/'.casefold())
@app.route('/Федя/'.casefold())
def fedor():
    return 'Привет, Федор!'

if __name__ == '__main__':
    app.run(debug=True)
