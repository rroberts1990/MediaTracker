from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User



class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About Me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class AddMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    genre = StringField('Genre')
    year = IntegerField('Year')
    watched = BooleanField('Watched?', validators=[DataRequired()])
    my_rating = IntegerField('My Rating')
    rt_rating = IntegerField('RT Rating')
    watched_date = DateField('Date Watched')
    tags = TextAreaField('Tags')
    submit = SubmitField('Add To List')


