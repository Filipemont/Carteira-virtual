from ext.database_ext import db

class Saida:

    __tablename__='Saida'
    __tableargs__={"schema":"register"}

    ID = db.Column(db.integer, primary_key=True)
    Descricao = db.Column(db.String(255))
    Valor = db.Column(db.Double)
    DataEntrada = db.Column(db.DateTime)
    DataRegistro = db.Column(db.DateTime)
    
    ID_Tipo_Saida = db.Column(db.Integer, db.ForeignKey('register.Tipo_de_Saida.ID'))
    ID_Usuario = db.Column(db.Integer, db.ForeignKey('register.Usuario.ID'))  
    