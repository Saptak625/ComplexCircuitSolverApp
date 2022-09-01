from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CircuitCodeForm(FlaskForm):
    circuitCode = TextAreaField('Circuit Code',
                        validators=[DataRequired()])
    submit = SubmitField('Submit')   