import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join('../app/db/mediatracker.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.sendgrid.net" #os.environ.get('MAIL_SERVER')
    MAIL_PORT = 587 #int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS =  1 #os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = 'apikey' #os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('SENDGRID_API_KEY')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    ADMINS = ['ross123roberts@gmail.com']
