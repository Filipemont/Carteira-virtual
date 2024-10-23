from ext.database_ext import db
from sqlalchemy.orm import relationship

class Entrada(db.Model):  
    __tablename__ = 'Entrada'
    __table_args__ = {"schema": "register"}

    ID = db.Column(db.Integer, primary_key=True)  
    Descricao = db.Column(db.String(255))
    Valor = db.Column(db.Float)  
    DataEntrada = db.Column(db.DateTime)
    DataRegistro = db.Column(db.DateTime)

    ID_Tipo_Entrada = db.Column(db.Integer, db.ForeignKey('register.Tipo_Entrada.ID'))
    ID_Usuario = db.Column(db.Integer, db.ForeignKey('register.Usuario.ID'))

    
    tipo_entrada = relationship("Tipo_Entrada", backref="entradas")  
    usuario = relationship("Usuario", backref="entradas")  
