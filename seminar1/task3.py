"""Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму.
"""

from task2 import *


@app.route('/sum/<int:num1>/<int:num2>/')
def sum_number(num1, num2):
    return f'{num1} + {num2} = {num1 + num2}'


if __name__ == '__main__':
    app.run(debug=True)