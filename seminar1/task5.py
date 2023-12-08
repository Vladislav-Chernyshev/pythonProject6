from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():
    html_text = """
    <h1>Hello world!</h1>
    <p>Second string</p>
    """
    return html_text


if __name__ == '__main__':
    app.run()
