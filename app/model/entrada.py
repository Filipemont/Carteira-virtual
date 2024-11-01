from ext.database_ext import db
from datetime import datetime


class Entrada(db.Model):
    __tablename__ = 'Entrada'
    __tableargs__ = {"schema": "register"}

    ID = db.Column(db.Integer, primary_key=True)
    Descricao = db.Column(db.String(255))
    Valor = db.Column(db.Float)
    DataEntrada = db.Column(db.DateTime(timezone=False),
                            nullable=True, default=lambda: datetime.now())
    DataRegistro = db.Column(db.DateTime(
        timezone=False), nullable=True, default=lambda: datetime.now())

    ID_Tipo_Entrada = db.Column(
        db.Integer, db.ForeignKey('register.Tipo_Entrada.ID'))
    Id_Usuario = db.Column(db.Integer, db.ForeignKey('register.Usuario.ID'))

    def to_dict(self):
        return {"Descricao": self.Descricao,
                "Valor": self.Valor,
                }
