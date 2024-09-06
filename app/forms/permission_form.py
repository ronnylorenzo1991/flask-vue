from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models.permission_model import Permission


class PermissionForm(FlaskForm):
    class Meta:
        csrf = False
    id = HiddenField('ID')    
    name = StringField(
        "Name", validators=[DataRequired(), Length(min=2, max=100)]
    )
    display_name = StringField(
        "Display Name", validators=[DataRequired(), Length(min=2, max=100)]
    )
    module_name = StringField(
        "Module Name", validators=[DataRequired(), Length(min=2, max=100)]
    )

    def validate_name(self, name):
        permission = Permission.query.filter_by(name=name.data).first()
        if permission and permission.id != self.id.data:
            raise ValidationError(
                "That permission name is taken. Please choose a different one."
            )

