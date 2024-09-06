from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models.role_model import Role


class RoleForm(FlaskForm):
    class Meta:
        csrf = False
    id = HiddenField('ID')    
    name = StringField(
        "Name", validators=[DataRequired(), Length(min=2, max=20)]
    )
    

    def validate_name(self, name):
        role = Role.query.filter_by(name=name.data).first()
        if role and role.id != self.id.data:
            raise ValidationError(
                "That role name is taken. Please choose a different one."
            )

