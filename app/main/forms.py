from flask_wtf import FlaskForm
from wtforms.validators import Required,Email
from wtforms import SubmitField, SelectField, TextAreaField, StringField,ValidationError
from ..models import User, Comment, Pitch

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')

class GeneralForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')
    
class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    body = TextAreaField('Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('Advertisement','Advertisement Pitch'),('Project','Project Pitch'),('General','General Pitch'),('Sale','Sale Pitch')], validators=[Required()])
    submit = SubmitField('Write Pitch!')

class CommentForm(FlaskForm):
    comment_content = TextAreaField('Write a comment', validators=[Required()])
    submit = SubmitField('Comment')

class GeneralReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')

class SaleForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class SaleReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')


class ProjectForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class ProjectReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')

class AdvertisementForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')

class AdvertisementReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')