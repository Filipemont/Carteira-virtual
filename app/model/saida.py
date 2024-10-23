from ext.database_ext import db
from sqlalchemy.orm import relationship

class Saida(db.Model): 
    __tablename__ = 'Saida'
    __table_args__ = {"schema": "register"}

    ID = db.Column(db.Integer, primary_key=True)
    Descricao = db.Column(db.String(255))
    Valor = db.Column(db.Float)  
    DataEntrada = db.Column(db.DateTime)
    DataRegistro = db.Column(db.DateTime)
    
    ID_Tipo_Saida = db.Column(db.Integer, db.ForeignKey('register.Tipo_de_Saida.ID'))
    ID_Usuario = db.Column(db.Integer, db.ForeignKey('register.Usuario.ID'))

    
    tipo_saida = relationship("Tipo_de_Saida", backref="saidas") 
    usuario = relationship("Usuario", backref="saidas")  
