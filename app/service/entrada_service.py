from repository.entrada_repository import EntradaRepository
from datetime import datetime

class EntradaService:
    __repository = EntradaRepository()

    def save(self, descricao, valor, data_entrada, id_tipo_entrada, id_usuario):
        data_criacao = '{' + datetime.now().strftime('%Y-%m-%d') +'}'
        self.__repository.insert(
            descricao, valor, data_entrada, data_criacao, id_tipo_entrada, id_usuario)

    def find_all(self):
        return self.__repository.get_all()

    def delete(self, id):
        self.__repository.delete_by_id(id)

    def findById(self, id):
        entrada = self.__repository.get_by_id(id)
        if entrada:
            return entrada

    def update(self, id, updated_data):
        entrada_atualizada = self.__repository.update(id, updated_data)
        return entrada_atualizada

    def find_by_tipo_entrada_id(self, tipo_entrada_id):
        return self.__repository.find_by_tipo_entrada(tipo_entrada_id)
    
    def find_by_usuario_id(self, usuario_id):
        return self.__repository.find_by_usuario_id(usuario_id)
