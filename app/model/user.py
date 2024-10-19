from ext.database_ext import db
class User:

    __tablename__='Usuario'
    __tableargs__={"schema":"register"}

    ID = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(60))
    Sobrenome = db.Column(db.String(60))
    Email = db.Column(db.String(255))
    Senha = db.Column(db.String(20))
    CPF = db.Column(db.String(11))
    Salt = db.Column(db.Integer) 

    
