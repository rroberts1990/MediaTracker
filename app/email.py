from flask_mail import Message
from flask import render_template
from app import mail, app

def send_email(subject, sender, recipients, text_body, text_html):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body=text_body
    msg.html=text_html
    mail.send(msg)

def send_password_reset_email(user):
    token = user.get_password_reset_token()
    send_email('[MediaTracker] Reset Your Password',
               sender=app.config['MAIL_DEFAULT_SENDER'],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
               user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))
