from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SubmitField, SelectMultipleField, HiddenField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app.models.user_model import User


class UserForm(FlaskForm):
    class Meta:
        csrf = False
    id = HiddenField('ID')    
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Submit")
    roles = SelectMultipleField("Roles", choices=[1,2])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user and user.id != self.id.data:
            raise ValidationError("That email is taken. Please choose a different one.")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user and user.id != self.id.data:
            raise ValidationError(
                "That username is taken. Please choose a different one."
            )


class LoginForm(FlaskForm):
    class Meta:
        csrf = False
        
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    password = StringField("Password", validators=[DataRequired()])
