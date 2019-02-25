from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index page test'


@app.route('/about')
def about():
    return 'About page test '


if __name__ == '__main__':
    app.run()
