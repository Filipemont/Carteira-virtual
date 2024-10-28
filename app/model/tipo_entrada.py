from ext.database_ext import db

class Tipo_Entrada(db.Model): 
    __tablename__ = 'Tipo_Entrada'
    __tableargs__ = {"schema": "register"}

    ID = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(255), nullable=False)  
    DataCriacao = db.Column(db.DateTime, nullable=False)  
    icone = db.Column(db.String(255))

    ID_Usuario = db.Column(db.Integer, db.ForeignKey('register.Usuario.ID'))
    
    
    usuario = db.relationship("User", backref="tipos_entrada") 
