from model.saida import Saida
from ext.database_ext import db


class SaidaRepository:
    def __init__(self):
        self.session = db.session

    def insert(self, descricao, valor, data_saida, id_tipo_saida, id_usuario):
        saida = Saida(Descricao=descricao, Valor=valor, Data_Vencimento=data_saida,
                      ID_Tipo_Saida=id_tipo_saida, ID_Usuario=id_usuario)
        self.session.add(saida)
        self.session.commit()

    def get_by_id(self, saida_id):
        return self.session.query(Saida).filter_by(ID=saida_id).first()

    def get_all(self):
        saidas = self.session.query(Saida).all()
        return [saida.to_dict() for saida in saidas]

    def delete_by_id(self, saida_id):
        saida = self.get_by_id(saida_id)
        if saida:
            self.session.delete(saida)
            self.session.commit()
            return saida
        return None

    def update(self, saida_id, updated_data):
        saida = self.get_by_id(saida_id)
        if saida:
            for key, value in updated_data.items():
                setattr(saida, key, value)
            self.session.commit()
            return saida
        return None

    def count(self):
        return self.session.query(Saida).count()

    def exists(self, saida_id):
        return self.session.query(Saida).filter_by(ID=saida_id).count() > 0

    def find_by_usuario_id(self, usuario_id):
        saidas = self.session.query(Saida).filter_by(Id_Usuario=usuario_id).all()
        return [saida.to_dict() for saida in saidas]

    def find_by_tipo_saida(self, tipo_saida_id):
        saidas = self.session.query(Saida).filter_by(ID_Tipo_Saida=tipo_saida_id).all()
        return [saida.to_dict() for saida in saidas]
