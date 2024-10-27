from model.tipo_saida import Tipo_de_Saida
from ext.database_ext import db


class TipoSaidaRepository:
    def __init__(self):
        self.session = db.session

    def get_by_id(self, tipo_saida_id):
        # Retorna um tipo de saída pelo ID.
        return self.session.query(Tipo_de_Saida).filter_by(ID=tipo_saida_id).first()

    def get_all(self):
        # Retorna todos os tipos de saída.
        return self.session.query(Tipo_de_Saida).all()

    def delete_by_id(self, tipo_saida_id):
        # Deleta um tipo de saída pelo ID e retorna o tipo deletado.
        tipo_saida = self.get_by_id(tipo_saida_id)
        if tipo_saida:
            self.session.delete(tipo_saida)
            self.session.commit()
            return tipo_saida
        return None

    def update(self, tipo_saida_id, updated_data):
        # Atualiza os dados de um tipo de saída existente.
        tipo_saida = self.get_by_id(tipo_saida_id)
        if tipo_saida:
            for key, value in updated_data.items():
                setattr(tipo_saida, key, value)
            self.session.commit()
            return tipo_saida
        return None

    def count(self):
        # Retorna a contagem total de tipos de saída.
        return self.session.query(Tipo_de_Saida).count()

    def exists(self, tipo_saida_id):
        # Verifica se um tipo de saída existe pelo ID.
        return self.session.query(Tipo_de_Saida).filter_by(ID=tipo_saida_id).count() > 0

    def find_by_usuario_id(self, usuario_id):
        # Retorna todos os tipos de saída associados a um usuário específico.
        return self.session.query(Tipo_de_Saida).filter_by(ID_Usuario=usuario_id).all()
