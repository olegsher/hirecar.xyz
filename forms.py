from flask_wtf import  Form
from wtforms import StringField, TextAreaField, SubmitField, HiddenField, ValidationError, validators, DateField



class ContactForm(Form):
 #   name = StringField("Name")
    name = StringField(u'Full Name', [validators.required(), validators.length(max=10)])
    email = StringField("Email")
    subject = StringField("Subject")
    message = TextAreaField("Message + car")
    #car = HiddenField("")
    submit = SubmitField("Send")