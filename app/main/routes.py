from app import db
from app.main.forms import EditProfileForm, EmptyForm, AddMovieForm, SearchForm
from app.main import bp
from app.models import User, Movie
from flask import render_template, flash, redirect, url_for, request, g, current_app
from flask_login import current_user, login_required
from collections import namedtuple
from datetime import datetime

MovieObject = namedtuple('Movie', 'title year genre director watched my_rating rt_rating watched_date tags')


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        g.search_form = SearchForm()

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie = Movie(title=form.title.data, year=form.year.data, genre=form.genre.data, director=form.director.data,
                      watched=form.watched.data, my_rating=form.my_rating.data, rt_rating=form.my_rating.data,
                      watched_date=form.watched_date.data, tags=form.tags.data)
        db.session.add(movie)
        db.session.commit()
        flash(f'You have just added {form.title.data} to your list.')
        return redirect(url_for('main.index'))
    posts = [
        {
            'author': {'username': 'John'},
            'record': MovieObject('Terminator 2',
                            '1991'
                           'Sci Fi',
                           'James Cameron',
                           'yes',
                           96,
                           93,
                           None,
                           "Time Travel")
        }
    ]
    return render_template('index.html', title='Home Page', form=form, post=posts)

#TODO: add redirect to login page when user clicks to add movie to their list
@bp.route('/explore')
def explore():
    movies = Movie.query.order_by(Movie.year.desc()).limit(20).all()
    return render_template('explore.html', title='Explore', posts=movies)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user.html', user=user, form=form)

@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash("Your changes have been made.")
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)


@bp.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash(f'User {username} not found')
            return redirect(url_for('main.index'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('main.user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash(f'You are now following {username}!')
        return redirect(url_for('main.user', username=username))
    else:
        return redirect(url_for('main.index'))


@bp.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('main.index'))
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('main.user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash('You are not following {}.'.format(username))
        return redirect(url_for('main.user', username=username))
    else:
        return redirect(url_for('main.index'))


@bp.route('/search')
@login_required
def search():
    if not g.search_form.validate():
        return redirect(url_for('main.explore'))
    page = request.args.get('page', 1, type=int)
    movies, total = Movie.search(g.search_form.q.data, page, current_app.config['POSTS_PER_PAGE'])
    next_url = url_for('main.search', q=g.search_form.q.data, page=page+1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page-1) \
        if page > 1 else None
    return render_template('search.html', title='Search', movies= movies, next_url=next_url, prev_url=prev_url)