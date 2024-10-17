from wtforms import Form, StringField, validators


class TipoEntradaForm(Form):
    nome = StringField('Nome da entrada', [
        validators.DataRequired(message="O nome é obrigatório.")
    ])
