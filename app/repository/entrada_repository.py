from model.entrada import Entrada
from ext.database_ext import db


class EntradaRepository:
    def __init__(self):
        self.session = db.session

    def get_by_id(self, entrada_id):
        # Retorna uma entrada pelo ID.
        return self.session.query(Entrada).filter_by(ID=entrada_id).first()

    def get_all(self):
        # Retorna todas as entradas.
        return self.session.query(Entrada).all()

    def delete_by_id(self, entrada_id):
        # Deleta uma entrada pelo ID e retorna a entrada deletada.
        entrada = self.get_by_id(entrada_id)
        if entrada:
            self.session.delete(entrada)
            self.session.commit()
            return entrada
        return None

    def update(self, entrada_id, updated_data):
        # Atualiza os dados de uma entrada existente.
        entrada = self.get_by_id(entrada_id)
        if entrada:
            for key, value in updated_data.items():
                setattr(entrada, key, value)
            self.session.commit()
            return entrada
        return None

    def count(self):
        # Retorna a contagem total de entradas.
        return self.session.query(Entrada).count()

    def exists(self, entrada_id):
        # Verifica se uma entrada existe pelo ID.
        return self.session.query(Entrada).filter_by(ID=entrada_id).count() > 0

    def find_by_usuario_id(self, usuario_id):
        # Retorna todas as entradas associadas a um usuário específico.
        return self.session.query(Entrada).filter_by(ID_Usuario=usuario_id).all()

    def find_by_tipo_entrada(self, tipo_entrada_id):
        # Retorna todas as entradas de um tipo específico.
        return self.session.query(Entrada).filter_by(ID_Tipo_Entrada=tipo_entrada_id).all()
