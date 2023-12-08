from task3 import *


@app.route('/str/<string:string1>/')
def get_str(string1):
    return string1


if __name__ == '__main__':
    app.run(debug=True)
