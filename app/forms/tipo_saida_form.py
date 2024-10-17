from wtforms import Form, StringField, validators


class TipoSaidaForm(Form):
    nome = StringField('Nome da saída', [
        validators.DataRequired(message="O nome é obrigatório.")
    ])
