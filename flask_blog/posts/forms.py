from flask_wtf import FlaskForm
from wtforms.validators import DataRequired 
from wtforms import SubmitField ,StringField ,TextAreaField

class PostForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    content=TextAreaField('Content',validators=[DataRequired()])
    submit= SubmitField('Post')

