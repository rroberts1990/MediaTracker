from app import app, db
from app.main.models import User, Book


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Book': Book}

if __name__ == '__main__':
    app.run(host='0.0.0.0')


