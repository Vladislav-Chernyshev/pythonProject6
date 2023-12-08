from flask import Flask

app = Flask(__name__)

html = """
<h1>Привет, меня зовут Алексей</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""


@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    return f'Привет {name.capitalize()}!'


@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'Путь до файла "{file}"'


@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Передано число {num}'


@app.route('/text/')
def text():
    return html


if __name__ == '__main__':
    app.run(debug=True)
