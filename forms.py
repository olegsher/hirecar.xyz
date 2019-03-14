from flask_wtf import  Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ContactForm(Form):
    name = StringField("Name")
    email = StringField("Email")
    subject = StringField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")