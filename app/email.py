from flask_mail import Message

from app import mail

def send_email(subject, sender, recipients, text_body, text_html):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body=text_body
    msg.html=text_html
    mail.send(msg)
