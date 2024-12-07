from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('Qual é o seu Nome?', validators=[DataRequired()])
    submit = SubmitField('submit')