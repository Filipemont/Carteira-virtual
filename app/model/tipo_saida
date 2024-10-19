from ext.database_ext import db

class Tipo_Entrada:

    __tablename__='Tipo_de_Saida'
    __tableargs__={"schema":"register"}

    ID = db.Column(db.integer, primary_key=True)
    Nome = db.Column(db.String(255))
    DataCriacao = db.Column(db.DateTime)
    icone = db.Column(db.String(255))
    DataRegistro = db.Column(db.DateTime)
    
    
    ID_Usuario = db.Column(db.Integer, db.ForeignKey('register.Usuario.ID'))  
    