from wtforms import Form, BooleanField, EmailField, PasswordField, validators


class Loginform(Form):
    email = EmailField('Email Address',
                       validators.DataRequired(),
                       )
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        [validators.Length(min=6, max=35)]
    ])

    remember = BooleanField('Remember me', [validators.DataRequired()])
