from flask import Flask, session, g, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/ru/index')
def index():
    title = "Прокат аренда авто в Израиле +972-58-7710101"
    paragraph = "Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("index.html", title = title, paragraph = paragraph)


@app.route('/ru/about')
def about():
    title = "About. Прокат аренда авто в Израиле +972-58-7710101"
    paragraph = "About/ Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("about.html", title=title, paragraph=paragraph)

@app.route('/ru/pricelist')
def pricelist():
    title = "Pricelist. Прокат аренда авто в Израиле +972-58-7710101"
    paragraph = "Privcelist/ Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("pricelist.html", title=title, paragraph=paragraph)


@app.route('/ru/minivan')
def minivan():
    title = "minivan. Прокат аренда авто в Израиле +972-58-7710101"
    paragraph = "Privcelist/ Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("minivan.html", title=title, paragraph=paragraph)

@app.route('/ru/lux')
def lux():
    title = "lux. Прокат аренда авто в Израиле +972-58-7710101"
    paragraph = "Privcelist/ Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("lux.html", title=title, paragraph=paragraph)

@app.route('/ru/budget')
def budget():
    title = "budget. Прокат аренда авто в Израиле +972-58-7710101"
    paragraph = "budget/ Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
    return render_template("budget.html", title=title, paragraph=paragraph)



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug = True)
