from wtforms import Form, StringField, DecimalField, DateField, validators


class EntradaForm(Form):
    descricao = StringField('Descrição', [
        validators.DataRequired(message="A descrição é obrigatória.")
    ])

    valor = DecimalField('Valor', [
        validators.DataRequired(message="O valor é obrigatório."),
        validators.NumberRange(
            min=0, message="O valor deve ser maior que zero.")
    ])

    data = DateField('Data da Entrada', [
        validators.DataRequired(message="A data é obrigatória.")
    ], format='%Y-%m-%d')
