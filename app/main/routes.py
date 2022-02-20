from app import app, db
from app.main.forms import EditProfileForm, EmptyForm, AddMovieForm
from app.main.models import User, Movie
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from collections import namedtuple
from datetime import datetime

Book = namedtuple('Book', 'title author genre publish_date read rating complete_date tags')

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie = Movie(title=form.title.data, genre=form.genre.data, year=form.year.data,
                      watched=form.watched.data, my_rating=form.my_rating.data, rt_rating=form.my_rating.data,
                      watched_date=form.watched_date.data, tags=form.tags.data)
        db.session.add(movie)
        db.session.commit()
        flash(f'You have just added {form.title.data} to your list.')
        return redirect(url_for('index'))
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
    return render_template('index.html', title='Home Page', form=form, post=posts)



@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
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
    form = EmptyForm()
    return render_template('user.html', user=user, posts=posts, form=form)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash("Your changes have been made.")
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)


@app.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash(f'User {username} not found')
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash(f'You are now following {username}!')
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))


@app.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash('You are not following {}.'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))

#TODO: add redirect to login page when user clicks to add movie to their list
@app.route('/explore')
def explore():
    movies = Movie.query.order_by(Movie.year.desc()).limit(20).all()
    return render_template('explore.html', title='Explore', posts=movies)

