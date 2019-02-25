from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index page test 1'


@app.route('/about')
def about():
    return 'About page test 1'


if __name__ == '__main__':
    app.run()
