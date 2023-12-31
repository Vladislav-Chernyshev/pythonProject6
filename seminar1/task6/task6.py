from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def fill_table():
    people = [
        {'Имя': 'Иван', 'Фамилия': 'Иванов', 'Возраст': 20,
         'Средний бал': 4.5},
        {'Имя': 'Петр', 'Фамилия': 'Петров', 'Возраст': 21,
         'Средний бал': 4.2},
        {'Имя': 'Сергей', 'Фамилия': 'Сергеев', 'Возраст': 19,
         'Средний бал': 4.8},
        {'Имя': 'Анна', 'Фамилия': 'Иванова', 'Возраст': 20,
         'Средний бал': 4.7}
    ]
    return render_template('index.html', students=people)

if __name__ == '__main__':
    app.run()
