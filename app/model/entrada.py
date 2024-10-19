from ext.database_ext import db

class Entrada:

    __tablename__='Entrada'
    __tableargs__={"schema":"register"}

    ID = db.Column(db.integer, primary_key=True)
    Descricao = db.Column(db.String(255))
    Valor = db.Column(db.Double)
    DataEntrada = db.Column(db.DateTime)
    DataRegistro = db.Column(db.DateTime)

    ID_Tipo_Entrada = db.Column(db.Integer, db.ForeignKey('register.Tipo_Entrada.ID'))  
    ID_Usuario = db.Column(db.Integer, db.ForeignKey('register.Usuario.ID'))
