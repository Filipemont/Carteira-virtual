from ext.database_ext import db
from datetime import datetime


class Tipo_de_Saida(db.Model):
    __tablename__ = 'Tipo_de_Saida'
    __tableargs__ = {"schema": "register"}

    ID = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(255), nullable=False)
    Data_Criacao = db.Column(db.DateTime(timezone=False),
                             nullable=True, default=lambda: datetime.now())
    icone = db.Column(db.String(255))

    Id_Usuario = db.Column(db.Integer, db.ForeignKey('register.Usuario.ID'))

    def to_dict(self):
        return {
                "Id": self.ID,
                "nome": self.Nome,
                "icone": self.icone,
                "Data_Criacao": self.Data_Criacao,
                "Id_Usuario": self.Id_Usuario
                }
