from repository.entrada_repository import EntradaRepository
from datetime import datetime


class EntradaService:
    __repository = EntradaRepository()

    def save(self, descricao, valor, data_entrada):
        data_registro = datetime.now()
        self.__repository.insert(descricao, valor, data_entrada, data_registro)

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
