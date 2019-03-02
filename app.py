from flask import Flask, session, g, render_template, json, request
from jinja2 import Template
from datetime import datetime
import json


app = Flask(__name__)

template = Template('''
    {% for mainkey in data %}
    <h1>{{ mainkey }}</h1>

    {% for key, value in data[mainkey].items() %}
    <p><strong>{{ key }}</strong><span>{{ value }}</span></p>
    {% endfor %}

    {% endfor %}
''')



json1_file = open('static/albar_pricelist.json')
json1_str = json1_file.read()
json1_data = json.loads(json1_str)
# pl_1 = json.loads('/albar_pricelist.json')

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}



@app.route('/p')
def p():
  title = "Прокат аренда авто в Израиле +972-58-7710101"
  paragraph = "Прокат аренда авто в Израиле. Отделения проката в Бен Гурион, Тель Авив Иерусалим Хайфа Эйлат Без предоплаты. Говорим по русски"
#    return render_template("p.html", title = title, paragraph = paragraph)
#    url = 'http://api.address'
#    response = requests.get(url)
#    data = response.json()

  return render_template("p.html", title = title, paragraph = paragraph)


@app.context_processor
def pl():
  return {'pl': json1_data }


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


pricelist_json : [
  {
    "Car Group": "B",
    "SIPP Code": "MBMR",
    "Group sig": 10,
    "Seats": 4,
    "Vehicle Type": "Suzuki Alto Man.",
    "Daily 1-2 Low": 10,
    "Daily 1-2 High": 22,
    "Daily 3-6 Low": 10,
    "Daily 3-6 High": 22,
    "Weekly-Low": 63,
    "Weekly-High": 147,
    "Ex. Day (8+)Low": 9,
    "Ex. Day (8+)High": 21,
    "Month (30+)Low": 610,
    "Month (30+)High": 790,
    "CDW": 10,
    "TP": 5,
    "3PLC": 12,
    "Extra KM": 0.45,
    "Super CDW": 10,
    "Super CDW Mothly": 100,
    "Super TP": 5,
    "Super TP monthly": 60,
    "Excess": 475
  },
  {
    "Car Group": "Q",
    "SIPP Code": "EBAR",
    "Group sig": 15,
    "Seats": 4,
    "Vehicle Type": "Fiat 500  (2 Doors)",
    "Daily 1-2 Low": 10,
    "Daily 1-2 High": 22,
    "Daily 3-6 Low": 10,
    "Daily 3-6 High": 22,
    "Weekly-Low": 63,
    "Weekly-High": 147,
    "Ex. Day (8+)Low": 9,
    "Ex. Day (8+)High": 21,
    "Month (30+)Low": 610,
    "Month (30+)High": 790,
    "CDW": 10,
    "TP": 5,
    "3PLC": 12,
    "Extra KM": 0.45,
    "Super CDW": 10,
    "Super CDW Mothly": 100,
    "Super TP": 5,
    "Super TP monthly": 60,
    "Excess": 475
  },
  {
    "Car Group": "C",
    "SIPP Code": "EDAR",
    "Group sig": 30,
    "Seats": 4,
    "Vehicle Type": "Kia Picanto",
    "Daily 1-2 Low": 11,
    "Daily 1-2 High": 23,
    "Daily 3-6 Low": 11,
    "Daily 3-6 High": 23,
    "Weekly-Low": 70,
    "Weekly-High": 154,
    "Ex. Day (8+)Low": 10,
    "Ex. Day (8+)High": 22,
    "Month (30+)Low": 620,
    "Month (30+)High": 800,
    "CDW": 10,
    "TP": 5,
    "3PLC": 12,
    "Extra KM": 0.45,
    "Super CDW": 10,
    "Super CDW Mothly": 100,
    "Super TP": 5,
    "Super TP monthly": 60,
    "Excess": 475
  },
  {
    "Car Group": "D",
    "SIPP Code": "CBAR",
    "Group sig": 20,
    "Seats": 4,
    "Vehicle Type": "Hyundai i20",
    "Daily 1-2 Low": 12,
    "Daily 1-2 High": 24,
    "Daily 3-6 Low": 12,
    "Daily 3-6 High": 24,
    "Weekly-Low": 77,
    "Weekly-High": 161,
    "Ex. Day (8+)Low": 11,
    "Ex. Day (8+)High": 23,
    "Month (30+)Low": 630,
    "Month (30+)High": 810,
    "CDW": 10,
    "TP": 5,
    "3PLC": 12,
    "Extra KM": 0.45,
    "Super CDW": 10,
    "Super CDW Mothly": 100,
    "Super TP": 5,
    "Super TP monthly": 60,
    "Excess": 475
  },
  {
    "Car Group": "E",
    "SIPP Code": "CCAR",
    "Group sig": 50,
    "Seats": 5,
    "Vehicle Type": "Ford Fiesta",
    "Daily 1-2 Low": 13,
    "Daily 1-2 High": 25,
    "Daily 3-6 Low": 13,
    "Daily 3-6 High": 25,
    "Weekly-Low": 84,
    "Weekly-High": 168,
    "Ex. Day (8+)Low": 12,
    "Ex. Day (8+)High": 24,
    "Month (30+)Low": 645,
    "Month (30+)High": 825,
    "CDW": 10,
    "TP": 5,
    "3PLC": 12,
    "Extra KM": 0.45,
    "Super CDW": 10,
    "Super CDW Mothly": 100,
    "Super TP": 5,
    "Super TP monthly": 60,
    "Excess": 475
  },
  {
    "Car Group": "F",
    "SIPP Code": "IDAR",
    "Group sig": 60,
    "Seats": 5,
    "Vehicle Type": "Hyundai Accent i25",
    "Daily 1-2 Low": 16,
    "Daily 1-2 High": 28,
    "Daily 3-6 Low": 16,
    "Daily 3-6 High": 28,
    "Weekly-Low": 98,
    "Weekly-High": 182,
    "Ex. Day (8+)Low": 14,
    "Ex. Day (8+)High": 26,
    "Month (30+)Low": 750,
    "Month (30+)High": 930,
    "CDW": 11,
    "TP": 5,
    "3PLC": 12,
    "Extra KM": 0.5,
    "Super CDW": 10,
    "Super CDW Mothly": 100,
    "Super TP": 5,
    "Super TP monthly": 60,
    "Excess": 475
  },
  {
    "Car Group": "I",
    "SIPP Code": "SCAR",
    "Group sig": 90,
    "Seats": 5,
    "Vehicle Type": "VW Golf",
    "Daily 1-2 Low": 18,
    "Daily 1-2 High": 30,
    "Daily 3-6 Low": 18,
    "Daily 3-6 High": 30,
    "Weekly-Low": 112,
    "Weekly-High": 196,
    "Ex. Day (8+)Low": 16,
    "Ex. Day (8+)High": 28,
    "Month (30+)Low": 790,
    "Month (30+)High": 970,
    "CDW": 11,
    "TP": 5,
    "3PLC": 12,
    "Extra KM": 0.5,
    "Super CDW": 10,
    "Super CDW Mothly": 100,
    "Super TP": 5,
    "Super TP monthly": 60,
    "Excess": 475
  },
  {
    "Car Group": "IW",
    "SIPP Code": "CWAR",
    "Group sig": 91,
    "Seats": 5,
    "Vehicle Type": "Seat Leon SW",
    "Daily 1-2 Low": 20,
    "Daily 1-2 High": 32,
    "Daily 3-6 Low": 20,
    "Daily 3-6 High": 32,
    "Weekly-Low": 126,
    "Weekly-High": 210,
    "Ex. Day (8+)Low": 18,
    "Ex. Day (8+)High": 30,
    "Month (30+)Low": 820,
    "Month (30+)High": 1000,
    "CDW": 11,
    "TP": 5,
    "3PLC": 12,
    "Extra KM": 0.5,
    "Super CDW": 10,
    "Super CDW Mothly": 100,
    "Super TP": 5,
    "Super TP monthly": 60,
    "Excess": 475
  },
  {
    "Car Group": "H",
    "SIPP Code": "SDAR",
    "Group sig": 80,
    "Seats": 5,
    "Vehicle Type": "VW Jetta",
    "Daily 1-2 Low": 24,
    "Daily 1-2 High": 36,
    "Daily 3-6 Low": 24,
    "Daily 3-6 High": 36,
    "Weekly-Low": 154,
    "Weekly-High": 238,
    "Ex. Day (8+)Low": 22,
    "Ex. Day (8+)High": 34,
    "Month (30+)Low": 960,
    "Month (30+)High": 1140,
    "CDW": 11,
    "TP": 5,
    "3PLC": 12,
    "Extra KM": 0.5,
    "Super CDW": 10,
    "Super CDW Mothly": 150,
    "Super TP": 5,
    "Super TP monthly": 70,
    "Excess": 715
  },
  {
    "Car Group": "M",
    "SIPP Code": "PDAR",
    "Group sig": 130,
    "Seats": 5,
    "Vehicle Type": "Mazda 6",
    "Daily 1-2 Low": 31,
    "Daily 1-2 High": 46,
    "Daily 3-6 Low": 31,
    "Daily 3-6 High": 46,
    "Weekly-Low": 196,
    "Weekly-High": 301,
    "Ex. Day (8+)Low": 28,
    "Ex. Day (8+)High": 43,
    "Month (30+)Low": 1050,
    "Month (30+)High": 1230,
    "CDW": 14,
    "TP": 5,
    "3PLC": 15,
    "Extra KM": 0.5,
    "Super CDW": 10,
    "Super CDW Mothly": 150,
    "Super TP": 7,
    "Super TP monthly": 70,
    "Excess": 715
  },
  {
    "Car Group": "MH",
    "SIPP Code": "PCAR",
    "Group sig": 135,
    "Seats": 5,
    "Vehicle Type": "Hyundai Sonata",
    "Daily 1-2 Low": 42,
    "Daily 1-2 High": 57,
    "Daily 3-6 Low": 42,
    "Daily 3-6 High": 57,
    "Weekly-Low": 266,
    "Weekly-High": 371,
    "Ex. Day (8+)Low": 38,
    "Ex. Day (8+)High": 53,
    "Month (30+)Low": 1450,
    "Month (30+)High": 1630,
    "CDW": 14,
    "TP": 5,
    "3PLC": 15,
    "Extra KM": 0.75,
    "Super CDW": 10,
    "Super CDW Mothly": 150,
    "Super TP": 7,
    "Super TP monthly": 70,
    "Excess": 715
  },
  {
    "Car Group": "K",
    "SIPP Code": "UDAR",
    "Group sig": 110,
    "Seats": 5,
    "Vehicle Type": "BMW 318i",
    "Daily 1-2 Low": 72,
    "Daily 1-2 High": 87,
    "Daily 3-6 Low": 72,
    "Daily 3-6 High": 87,
    "Weekly-Low": 455,
    "Weekly-High": 560,
    "Ex. Day (8+)Low": 65,
    "Ex. Day (8+)High": 80,
    "Month (30+)Low": 1590,
    "Month (30+)High": 1770,
    "CDW": 14,
    "TP": 5,
    "3PLC": 15,
    "Extra KM": 0.75,
    "Super CDW": 10,
    "Super CDW Mothly": 150,
    "Super TP": 7,
    "Super TP monthly": 70,
    "Excess": 715
  },
  {
    "Car Group": "R",
    "SIPP Code": "FCAR",
    "Group sig": 180,
    "Seats": 5,
    "Vehicle Type": "VW Passat",
    "Daily 1-2 Low": 58,
    "Daily 1-2 High": 73,
    "Daily 3-6 Low": 58,
    "Daily 3-6 High": 73,
    "Weekly-Low": 364,
    "Weekly-High": 469,
    "Ex. Day (8+)Low": 52,
    "Ex. Day (8+)High": 67,
    "Month (30+)Low": 1640,
    "Month (30+)High": 1820,
    "CDW": 14,
    "TP": 5,
    "3PLC": 15,
    "Extra KM": 0.75,
    "Super CDW": 15,
    "Super CDW Mothly": 210,
    "Super TP": 10,
    "Super TP monthly": 90,
    "Excess": 960
  },
  {
    "Car Group": "P",
    "SIPP Code": "LDAR",
    "Group sig": 160,
    "Seats": 5,
    "Vehicle Type": "Nissan Maxima",
    "Daily 1-2 Low": 79,
    "Daily 1-2 High": 109,
    "Daily 3-6 Low": 79,
    "Daily 3-6 High": 109,
    "Weekly-Low": 497,
    "Weekly-High": 707,
    "Ex. Day (8+)Low": 71,
    "Ex. Day (8+)High": 101,
    "Month (30+)Low": 2170,
    "Month (30+)High": 2410,
    "CDW": 35,
    "TP": 10,
    "3PLC": 40,
    "Extra KM": 0.75,
    "Super CDW": 15,
    "Super CDW Mothly": 210,
    "Super TP": 10,
    "Super TP monthly": 90,
    "Excess": 960
  },
  {
    "Car Group": "W",
    "SIPP Code": "LCBR",
    "Group sig": 230,
    "Seats": 5,
    "Vehicle Type": "Audi A6",
    "Daily 1-2 Low": 122,
    "Daily 1-2 High": 152,
    "Daily 3-6 Low": 122,
    "Daily 3-6 High": 152,
    "Weekly-Low": 770,
    "Weekly-High": 980,
    "Ex. Day (8+)Low": 110,
    "Ex. Day (8+)High": 140,
    "Month (30+)Low": 2690,
    "Month (30+)High": 2930,
    "CDW": 35,
    "TP": 10,
    "3PLC": 40,
    "Extra KM": 0.75,
    "Super CDW": 15,
    "Super CDW Mothly": 210,
    "Super TP": 10,
    "Super TP monthly": 90,
    "Excess": 960
  },
  {
    "Car Group": "FX",
    "SIPP Code": "DBAR",
    "Group sig": 65,
    "Seats": 5,
    "Vehicle Type": "Renault Megane Coupe (2 Doors)",
    "Daily 1-2 Low": 17,
    "Daily 1-2 High": 29,
    "Daily 3-6 Low": 17,
    "Daily 3-6 High": 29,
    "Weekly-Low": 105,
    "Weekly-High": 189,
    "Ex. Day (8+)Low": 15,
    "Ex. Day (8+)High": 27,
    "Month (30+)Low": 760,
    "Month (30+)High": 940,
    "CDW": 11,
    "TP": 5,
    "3PLC": 12,
    "Extra KM": 0.5,
    "Super CDW": 10,
    "Super CDW Mothly": 100,
    "Super TP": 5,
    "Super TP monthly": 60,
    "Excess": 475
  },
  {
    "Car Group": "T",
    "SIPP Code": "CPMR",
    "Group sig": 200,
    "Seats": 5,
    "Vehicle Type": "VW Caddy Man.",
    "Daily 1-2 Low": 39,
    "Daily 1-2 High": 69,
    "Daily 3-6 Low": 39,
    "Daily 3-6 High": 69,
    "Weekly-Low": 245,
    "Weekly-High": 455,
    "Ex. Day (8+)Low": 35,
    "Ex. Day (8+)High": 65,
    "Month (30+)Low": 1050,
    "Month (30+)High": 1290,
    "CDW": 15,
    "TP": 10,
    "3PLC": 20,
    "Extra KM": 0.75,
    "Super CDW": 10,
    "Super CDW Mothly": 100,
    "Super TP": 5,
    "Super TP monthly": 60,
    "Excess": 475
  },
  {
    "Car Group": "J",
    "SIPP Code": "SFBR",
    "Group sig": 100,
    "Seats": 5,
    "Vehicle Type": "Hyundai Tucson Aut.",
    "Daily 1-2 Low": 42,
    "Daily 1-2 High": 72,
    "Daily 3-6 Low": 42,
    "Daily 3-6 High": 72,
    "Weekly-Low": 266,
    "Weekly-High": 476,
    "Ex. Day (8+)Low": 38,
    "Ex. Day (8+)High": 68,
    "Month (30+)Low": 1240,
    "Month (30+)High": 1480,
    "CDW": 15,
    "TP": 10,
    "3PLC": 20,
    "Extra KM": 0.75,
    "Super CDW": 10,
    "Super CDW Mothly": 150,
    "Super TP": 7,
    "Super TP monthly": 70,
    "Excess": 715
  },
  {
    "Car Group": "O",
    "SIPP Code": "LFBR",
    "Group sig": 150,
    "Seats": 5,
    "Vehicle Type": "Ford Edge Aut.",
    "Daily 1-2 Low": 74,
    "Daily 1-2 High": 104,
    "Daily 3-6 Low": 74,
    "Daily 3-6 High": 104,
    "Weekly-Low": 469,
    "Weekly-High": 679,
    "Ex. Day (8+)Low": 67,
    "Ex. Day (8+)High": 97,
    "Month (30+)Low": 2250,
    "Month (30+)High": 2550,
    "CDW": 35,
    "TP": 10,
    "3PLC": 40,
    "Extra KM": 0.75,
    "Super CDW": 15,
    "Super CDW Mothly": 210,
    "Super TP": 10,
    "Super TP monthly": 90,
    "Excess": 960
  },
  {
    "Car Group": "U",
    "SIPP Code": "IVAR",
    "Group sig": 210,
    "Seats": 7,
    "Vehicle Type": "Opel Zafira Aut.",
    "Daily 1-2 Low": 39,
    "Daily 1-2 High": 69,
    "Daily 3-6 Low": 39,
    "Daily 3-6 High": 69,
    "Weekly-Low": 245,
    "Weekly-High": 455,
    "Ex. Day (8+)Low": 35,
    "Ex. Day (8+)High": 65,
    "Month (30+)Low": 1220,
    "Month (30+)High": 1520,
    "CDW": 15,
    "TP": 10,
    "3PLC": 20,
    "Extra KM": 0.75,
    "Super CDW": 15,
    "Super CDW Mothly": 210,
    "Super TP": 10,
    "Super TP monthly": 90,
    "Excess": 715
  },
  {
    "Car Group": "V",
    "SIPP Code": "SVAR",
    "Group sig": 220,
    "Seats": 7,
    "Vehicle Type": "Mitsubishi Outlander Aut.",
    "Daily 1-2 Low": 58,
    "Daily 1-2 High": 88,
    "Daily 3-6 Low": 58,
    "Daily 3-6 High": 88,
    "Weekly-Low": 364,
    "Weekly-High": 574,
    "Ex. Day (8+)Low": 52,
    "Ex. Day (8+)High": 82,
    "Month (30+)Low": 1550,
    "Month (30+)High": 1850,
    "CDW": 15,
    "TP": 10,
    "3PLC": 20,
    "Extra KM": 0.75,
    "Super CDW": 15,
    "Super CDW Mothly": 210,
    "Super TP": 10,
    "Super TP monthly": 90,
    "Excess": 960
  },
  {
    "Car Group": "V8",
    "SIPP Code": "FVAR",
    "Group sig": 225,
    "Seats": 8,
    "Vehicle Type": "Kia Carnival Aut.",
    "Daily 1-2 Low": 83,
    "Daily 1-2 High": 113,
    "Daily 3-6 Low": 83,
    "Daily 3-6 High": 113,
    "Weekly-Low": 525,
    "Weekly-High": 735,
    "Ex. Day (8+)Low": 75,
    "Ex. Day (8+)High": 105,
    "Month (30+)Low": 1870,
    "Month (30+)High": 2170,
    "CDW": 35,
    "TP": 10,
    "3PLC": 40,
    "Extra KM": 0.75,
    "Super CDW": 15,
    "Super CDW Mothly": 210,
    "Super TP": 10,
    "Super TP monthly": 90,
    "Excess": 960
  },
  {
    "Car Group": "Y",
    "SIPP Code": "FVMR",
    "Group sig": 250,
    "Seats": 9,
    "Vehicle Type": "Renault Traffic Man.",
    "Daily 1-2 Low": 55,
    "Daily 1-2 High": 85,
    "Daily 3-6 Low": 55,
    "Daily 3-6 High": 85,
    "Weekly-Low": 343,
    "Weekly-High": 553,
    "Ex. Day (8+)Low": 49,
    "Ex. Day (8+)High": 79,
    "Month (30+)Low": 1600,
    "Month (30+)High": 1900,
    "CDW": 35,
    "TP": 10,
    "3PLC": 40,
    "Extra KM": 0.75,
    "Super CDW": 15,
    "Super CDW Mothly": 210,
    "Super TP": 10,
    "Super TP monthly": 90,
    "Excess": 960
  },
  {
    "Car Group": "Z",
    "SIPP Code": "LVAR",
    "Group sig": 260,
    "Seats": 9,
    "Vehicle Type": "VW Transporter Aut.",
    "Daily 1-2 Low": 95,
    "Daily 1-2 High": 125,
    "Daily 3-6 Low": 95,
    "Daily 3-6 High": 125,
    "Weekly-Low": 602,
    "Weekly-High": 812,
    "Ex. Day (8+)Low": 86,
    "Ex. Day (8+)High": 116,
    "Month (30+)Low": 2120,
    "Month (30+)High": 2420,
    "CDW": 35,
    "TP": 10,
    "3PLC": 40,
    "Extra KM": 0.75,
    "Super CDW": 15,
    "Super CDW Mothly": 210,
    "Super TP": 10,
    "Super TP monthly": 90,
    "Excess": 960
  }
]


if __name__ == '__main__':
    app.run(debug = True)