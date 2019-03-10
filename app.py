from flask import Flask, session, g, render_template, json, request, flash
from jinja2 import Template
from datetime import datetime
from flask_mail import Mail, Message

#from flask_wtf import FlaskForm
#from wtforms import StringField
#from wtforms.validators import DataRequired


app = Flask(__name__)


mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'admin@sher.biz',
    "MAIL_PASSWORD": '!!!os345o'
}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    with app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["test@sher.biz"], # replace with your email for testing
                      body="This is a test email I sent with Gmail and Python!")
        mail.send(msg)

json1_file = open('static/albar_pricelist.json')
json1_str = json1_file.read()
albar_dict = json.loads(json1_str)


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.context_processor
def pl():
  return {'pl': albar_dict }


@app.context_processor
def pl_size():
    return {'pl_size': len(albar_dict)}


@app.route('/p')
def p():
  title = "Прокат аренда авто в Израиле +972-58-7710101"
  meta_description = "Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
  return render_template("p.html", title = title, meta_description = meta_description)


@app.route('/')
@app.route('/ru/index')
def index():
    title = "Прокат аренда авто в Израиле +972-58-7710101"
    meta_description = "Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("index.html", title = title, meta_description = meta_description)


@app.route('/ru/about')
def about():
    title = "About. Прокат аренда авто в Израиле +972-58-7710101"
    meta_description = "About/ Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("about.html", title=title, meta_description = meta_description)

@app.route('/ru/pricelist')
def pricelist():
    title = "Pricelist. Прокат аренда авто в Израиле +972-58-7710101"
    meta_description = "Privcelist/ Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("pricelist.html", title=title, meta_description = meta_description)


@app.route('/ru/minivan')
def minivan():
    title = "minivan. Прокат аренда авто в Израиле +972-58-7710101"
    meta_description = "Privcelist/ Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("minivan.html", title=title, meta_description = meta_description)

@app.route('/ru/lux')
def lux():
    title = "lux. Прокат аренда авто в Израиле +972-58-7710101"
    meta_description = "Privcelist/ Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("lux.html", title=title, meta_description = meta_description)

@app.route('/ru/budget')
def budget():
    title = "budget. Прокат аренда авто в Израиле +972-58-7710101"
    meta_description = "budget/ Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("budget.html", title=title, meta_description = meta_description)

@app.route('/menu')
def _menu():
    title = "menu. test"
    meta_description = "menu"
    return render_template("budget.html", title=title, meta_description=meta_description)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)