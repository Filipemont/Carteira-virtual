from model.tipo_saida import Tipo_de_Saida
from ext.database_ext import db


class TipoSaidaRepository:
    def __init__(self):
        self.session = db.session

    def insert(self, nome, icone , id_usuario):
        tipo_de_saida = Tipo_de_Saida(
            Nome=nome, icone=icone, Id_Usuario=id_usuario)
        self.session.add(tipo_de_saida)
        self.session.commit()

    def get_by_id(self, tipo_saida_id):
        tipo_de_saida = self.session.query(Tipo_de_Saida).filter_by(ID=tipo_saida_id).first()
        return tipo_de_saida.to_dict()

    def get_all(self):
        tipos_de_saidas = self.session.query(Tipo_de_Saida).all()
        return [tipo_de_saida.to_dict() for tipo_de_saida in tipos_de_saidas]

    def delete_by_id(self, tipo_saida_id):
        tipo_saida = self.session.query(Tipo_de_Saida).filter_by(ID=tipo_saida_id).first()
        if tipo_saida:
            self.session.delete(tipo_saida)
            self.session.commit()
            return tipo_saida
        return None

    def update(self, tipo_saida_id, updated_data):
        tipo_saida = self.get_by_id(tipo_saida_id)
        if tipo_saida:
            for key, value in updated_data.items():
                setattr(tipo_saida, key, value)
            self.session.commit()
            return tipo_saida
        return None

    def count(self):
        return self.session.query(Tipo_de_Saida).count()

    def exists(self, tipo_saida_id):
        return self.session.query(Tipo_de_Saida).filter_by(ID=tipo_saida_id).count() > 0

    def find_by_usuario_id(self, usuario_id):
        tipos_de_saidas = self.session.query(Tipo_de_Saida).filter_by(Id_Usuario=usuario_id).all()
        return [tipo_de_saida.to_dict() for tipo_de_saida in tipos_de_saidas]

