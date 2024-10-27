from repository.tipo_saida_repository import TipoSaidaRepository
from datetime import datetime


class TipoSaidaService:
    __repository = TipoSaidaRepository()

    def save(self, nome, icone):
        data_criacao = datetime.now()
        self.__repository.insert(nome, data_criacao, icone)

    def find_all(self):
        return self.__repository.get_all()

    def delete(self, id):
        self.__repository.delete_by_id(id)

    def findById(self, id):
        tipo_saida = self.__repository.get_by_id(id)
        if tipo_saida:
            return tipo_saida
