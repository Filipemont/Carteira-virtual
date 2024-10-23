from ext.database_ext import db
from sqlalchemy.orm import relationship

class Tipo_Entrada(db.Model): 
    __tablename__ = 'Tipo_Entrada'
    __tableargs__ = {"schema": "register"}

    ID = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(255), nullable=False)  
    DataCriacao = db.Column(db.DateTime, nullable=False)  
    icone = db.Column(db.String(255))
    DataRegistro = db.Column(db.DateTime)

    ID_Usuario = db.Column(db.Integer, db.ForeignKey('register.Usuario.ID'))
    
    
    usuario = relationship("User", backref="tipos_entrada") 
