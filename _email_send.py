from flask import Flask, session, g, render_template, json, request, flash
from jinja2 import Template
from datetime import datetime
from flask_mail import Mail, Message



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
                      sender="admin@sher.biz",
                      recipients=["test@sher.biz"], # replace with your email for testing
                      body="This is a test email I sent with Gmail and Python!")
        mail.send(msg)