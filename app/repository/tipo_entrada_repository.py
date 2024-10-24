from model.tipo_entrada import Tipo_Entrada

class TipoEntradaRepository:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, tipo_entrada_id):
        # Retorna um tipo de entrada pelo ID.
        return self.session.query(Tipo_Entrada).filter_by(ID=tipo_entrada_id).first()

    def get_all(self):
        # Retorna todos os tipos de entrada.
        return self.session.query(Tipo_Entrada).all()

    def delete_by_id(self, tipo_entrada_id):
        # Deleta um tipo de entrada pelo ID e retorna o tipo deletado.
        tipo_entrada = self.get_by_id(tipo_entrada_id)
        if tipo_entrada:
            self.session.delete(tipo_entrada)
            self.session.commit()
            return tipo_entrada
        return None

    def update(self, tipo_entrada_id, updated_data):
        # Atualiza os dados de um tipo de entrada existente.
        tipo_entrada = self.get_by_id(tipo_entrada_id)
        if tipo_entrada:
            for key, value in updated_data.items():
                setattr(tipo_entrada, key, value)
            self.session.commit()
            return tipo_entrada
        return None

    def count(self):
        # Retorna a contagem total de tipos de entrada.
        return self.session.query(Tipo_Entrada).count()

    def exists(self, tipo_entrada_id):
        # Verifica se um tipo de entrada existe pelo ID.
        return self.session.query(Tipo_Entrada).filter_by(ID=tipo_entrada_id).count() > 0

    def find_by_usuario_id(self, usuario_id):
        # Retorna todos os tipos de entrada associados a um usuário específico.
        return self.session.query(Tipo_Entrada).filter_by(ID_Usuario=usuario_id).all()
