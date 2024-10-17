from wtforms import Form, SubmitField, StringField, PasswordField, validators, EmailField, ValidationError
import re


def validate_password(form, field):
    password = field.data
    if not re.search(r'[A-Z]', password):
        raise ValidationError(
            'A senha deve conter pelo menos uma letra maiúscula.')
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError(
            'A senha deve conter pelo menos um caractere especial.')


def validate_cpf(form, field):
    cpf = re.sub(r'\D', '', field.data)
    if len(cpf) != 11:
        raise ValidationError('O CPF deve conter 11 dígitos.')

    def cpf_verifier(cpf):
        if cpf == cpf[0] * len(cpf):
            return False

        for i in range(9, 11):
            value = sum((int(cpf[num]) * ((i+1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if digit != int(cpf[i]):
                return False
        return True

    if not cpf_verifier(cpf):
        raise ValidationError('CPF inválido.')


class Registerform(Form):
    nome = StringField('Nome',
                       validators.DataRequired(),)
    nome = StringField('Sobrenome',
                       validators.DataRequired(),)
    email = EmailField('Email', [
                       validators.DataRequired(),
                       validators.EqualTo(
                           'emailconfirm', message='Os email deve ser igual.'),
                       ])
    emailconfirm = EmailField('Confirmação de Email',
                              validators.DataRequired(),
                              )
    password = PasswordField('Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='As senhas devem ser iguais.'),
        validators.Length(
            min=8, max=20, message='A senha deve ter entre 8 e 20 caracteres.'),
        validate_password
    ])
    cpf = StringField('CPF', [
        validators.DataRequired(),
        validate_cpf
    ])

    confirm = PasswordField('Confirme a senha',
                            validators.DataRequired())

    submit = SubmitField('Submit')
