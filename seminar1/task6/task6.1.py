from flask import Flask
from flask import render_template
from tabulate import tabulate
import pandas as pd

app = Flask(__name__)


@app.route('/students/')
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

    # html_table = tabulate(people, headers='keys', tablefmt='html')
    html_table = pd.DataFrame(people).to_html()

    print(html_table)
    return render_template('students.html', people=html_table)


if __name__ == '__main__':
    app.run()