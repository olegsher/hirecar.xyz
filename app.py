from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index page test 11'


@app.route('/about')
def about():
    return 'About page test 11'


if __name__ == '__main__':
    app.run()
