from repository.saida_repository import SaidaRepository
from datetime import datetime


class SaidaService:
    __repository = SaidaRepository()

    def save(self, descricao, valor, data_entrada):
        data_registro = datetime.now()
        self.__repository.insert(descricao, valor, data_entrada, data_registro)

    def find_all(self):
        return self.__repository.get_all()

    def delete(self, id):
        self.__repository.delete_by_id(id)

    def findById(self, id):
        saida = self.__repository.get_by_id(id)
        if saida:
            return saida
        