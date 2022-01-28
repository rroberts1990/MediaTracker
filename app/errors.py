from flask import render_template
from app import app, db
from flask_mail import Mail, Message

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    mail=Mail(app)
    msg=Message(error, recipients=['ross123roberts@gmail.com'])
    msg.body=error
    msg.html=f'<p>{error}</p>'
    mail.send(msg)
    return render_template('500.html'), 500