from model.saida import Saida

class SaidaRepository:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, saida_id):
        # Retorna uma saída pelo ID.
        return self.session.query(Saida).filter_by(ID=saida_id).first()

    def get_all(self):
        # Retorna todas as saídas.
        return self.session.query(Saida).all()

    def delete_by_id(self, saida_id):
        # Deleta uma saída pelo ID e retorna a saída deletada.
        saida = self.get_by_id(saida_id)
        if saida:
            self.session.delete(saida)
            self.session.commit()
            return saida
        return None

    def update(self, saida_id, updated_data):
        # Atualiza os dados de uma saída existente.
        saida = self.get_by_id(saida_id)
        if saida:
            for key, value in updated_data.items():
                setattr(saida, key, value)
            self.session.commit()
            return saida
        return None

    def count(self):
        # Retorna a contagem total de saídas.
        return self.session.query(Saida).count()

    def exists(self, saida_id):
        # Verifica se uma saída existe pelo ID.
        return self.session.query(Saida).filter_by(ID=saida_id).count() > 0

    def find_by_usuario_id(self, usuario_id):
        # Retorna todas as saídas associadas a um usuário específico.
        return self.session.query(Saida).filter_by(ID_Usuario=usuario_id).all()

    def find_by_tipo_saida(self, tipo_saida_id):
        # Retorna todas as saídas de um tipo específico.
        return self.session.query(Saida).filter_by(ID_Tipo_Saida=tipo_saida_id).all()
