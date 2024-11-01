from ext.database_ext import db
from datetime import datetime


class Saida(db.Model):
    __tablename__ = 'Saida'
    __tableargs__ = {"schema": "register"}

    ID = db.Column(db.Integer, primary_key=True)
    Descricao = db.Column(db.String(255))
    Valor = db.Column(db.Float)
    DataSaida = db.Column(db.DateTime(timezone=False),
                          nullable=True, default=lambda: datetime.now())
    DataRegistro = db.Column(db.DateTime(
        timezone=False), nullable=True, default=lambda: datetime.now())

    ID_Tipo_Saida = db.Column(
        db.Integer, db.ForeignKey('register.Tipo_de_Saida.ID'))
    ID_Usuario = db.Column(db.Integer, db.ForeignKey('register.Usuario.ID'))

    tipo_saida = db.relationship("Tipo_de_Saida", backref="saidas")
    usuario = db.relationship("Usuario", backref="saidas")
