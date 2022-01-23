from app import app
from flask import render_template, flash, redirect, url_for
from collections import namedtuple
from app.forms import LoginForm

Book = namedtuple('Book', 'title author genre publish_date read rating complete_date tags')

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'rroberts1990'}
    posts = [
        {
            'author': {'username': 'John'},
            'record': Book('The Lies of Locke Lamora',
                           'Scott Lynch',
                           'Fantasy',
                           '2006-06-27',
                           1,
                           95,
                           "01-01-2015",
                           "Gentleman Bastards")
        },
        {
            'author': {'username': 'Susan'},
            'record': Book('The Way of Kings',
                           'Brandon Sanderson',
                           'Fantasy',
                           '2010-08-31',
                           1,
                           91,
                           "01-01-2019",
                           "Cosmere Stormlight Archive")
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
