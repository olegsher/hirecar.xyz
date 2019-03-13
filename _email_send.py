from flask_mail import Message
from app import mail

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'admin@sher.biz',
    "MAIL_PASSWORD": '!!!os345o'
}


@mail.route('/send-mail/')
def send_mail():
    msg = mail.send_message(
        'Send Mail tutorial!',
        sender='ri******a@gmail.com',
        recipients=['ri*********07@msn.com'],
        body="Congratulations you've succeeded!"
    )
    return 'Mail sent'


