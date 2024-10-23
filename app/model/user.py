from ext.database_ext import db

class User(db.Model): 
    __tablename__ = 'Usuario'
    __tableargs__ = {"schema": "register"}

    ID = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(60), nullable=False)  
    Sobrenome = db.Column(db.String(60), nullable=False)  
    Email = db.Column(db.String(255), nullable=False, unique=True) 
    Senha = db.Column(db.String(100), nullable=False)  
    CPF = db.Column(db.String(11), nullable=False, unique=True)  
    Salt = db.Column(db.LargeBinary)  

