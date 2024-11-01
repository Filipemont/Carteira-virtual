from model.tipo_entrada import Tipo_Entrada
from ext.database_ext import db


class TipoEntradaRepository:
    def __init__(self):
        self.session = db.session

    def insert(self, nome, data_criacao, icone,):
        tipo_de_entrada = Tipo_Entrada(
            Nome=nome, DataCriacao=data_criacao, icone=icone)
        self.session.add(tipo_de_entrada)
        self.session.commit()

    def get_by_id(self, tipo_entrada_id):
        return self.session.query(Tipo_Entrada).filter_by(ID=tipo_entrada_id).first()

    def get_all(self):
        tipos_de_entrada = self.session.query(Tipo_Entrada).all()
        return [tipo_de_entrada.to_dict() for tipo_de_entrada in tipos_de_entrada]

    def delete_by_id(self, tipo_entrada_id):
        tipo_entrada = self.get_by_id(tipo_entrada_id)
        if tipo_entrada:
            self.session.delete(tipo_entrada)
            self.session.commit()
            return tipo_entrada
        return None

    def update(self, tipo_entrada_id, updated_data):
        tipo_entrada = self.get_by_id(tipo_entrada_id)
        if tipo_entrada:
            for key, value in updated_data.items():
                setattr(tipo_entrada, key, value)
            self.session.commit()
            return tipo_entrada
        return None

    def count(self):
        return self.session.query(Tipo_Entrada).count()

    def exists(self, tipo_entrada_id):
        return self.session.query(Tipo_Entrada).filter_by(ID=tipo_entrada_id).count() > 0

    def find_by_usuario_id(self, usuario_id):
        return self.session.query(Tipo_Entrada).filter_by(ID_Usuario=usuario_id).all()
