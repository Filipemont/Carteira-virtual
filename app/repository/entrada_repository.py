from model.entrada import Entrada
from ext.database_ext import db


class EntradaRepository:
    def __init__(self):
        self.session = db.session

    def insert(self, descricao, valor, data_entrada, id_tipo_entrada, id_usuario):
        entrada = Entrada(Descricao=descricao, Valor=valor, DataEntrada=data_entrada,
                          ID_Tipo_Entrada=id_tipo_entrada, Id_Usuario=id_usuario)
        self.session.add(entrada)
        self.session.commit()

    def get_by_id(self, entrada_id):
        return self.session.query(Entrada).filter_by(ID=entrada_id).first()

    def get_all(self):
        entradas = self.session.query(Entrada).all()
        return [entrada.to_dict() for entrada in entradas]

    def delete_by_id(self, entrada_id):
        entrada = self.get_by_id(entrada_id)
        if entrada:
            self.session.delete(entrada)
            self.session.commit()
            return entrada
        return None

    def update(self, entrada_id, updated_data):
        entrada = self.get_by_id(entrada_id)
        if entrada:
            for key, value in updated_data.items():
                setattr(entrada, key, value)
            self.session.commit()
            return entrada
        return None

    def count(self):
        return self.session.query(Entrada).count()

    def exists(self, entrada_id):
        return self.session.query(Entrada).filter_by(ID=entrada_id).count() > 0

    def find_by_usuario_id(self, usuario_id):
        entradas = self.session.query(Entrada).filter_by(Id_Usuario=usuario_id).all()
        return [entrada.to_dict() for entrada in entradas]

    def find_by_tipo_entrada(self, tipo_entrada_id):
        entradas = self.session.query(Entrada).filter_by(ID_Tipo_Entrada=tipo_entrada_id).all()
        return [entrada.to_dict() for entrada in entradas]
