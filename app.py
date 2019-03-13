from flask import Flask, session, g, render_template, json, request, flash
from jinja2 import Template
from datetime import datetime
from flask_mail import Mail, Message
import os

app = Flask(__name__)


app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')


app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True
)

mail = Mail(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


#Development


@app.route('/send-mail')
#@app.context_processor
def send_mail():
    msg = mail.send_message(
        'Send Mail tutorial!',
        sender='test@sher.biz',
        recipients=['test@sher.biz'],
        body="Congratulations you've succeeded!"
    )
    return 'Mail sent'



#End of development

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
  return render_template("form.html", title = title, meta_description = meta_description)

@app.route('/contact_form')
def contact_form():
    title = "Прокат аренда авто в Израиле +972-58-7710101"
    meta_description = "Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("contact_form.html", title = title, meta_description = meta_description)


@app.route('/')
@app.route('/ru/index')
def index():
    flash('You were successfully logged in')
    title = "Прокат аренда авто в Израиле +972-58-7710101"
    meta_description = "Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("index.html", title = title, meta_description = meta_description)


@app.route('/ru/index_2')
def index_2():
    title = "Прокат аренда авто в Израиле +972-58-7710101"
    meta_description = "Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("index_2.html", title = title, meta_description = meta_description)


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
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)