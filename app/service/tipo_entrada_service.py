from repository.tipo_entrada_repository import TipoEntradaRepository
from datetime import datetime


class TipoEntradaService:
    __repository = TipoEntradaRepository()

    def save(self, nome, icone):
        data_criacao = datetime.now()
        self.__repository.insert(nome, data_criacao, icone)

    def find_all(self):
        return self.__repository.get_all()

    def delete(self, id):
        self.__repository.delete_by_id(id)

    def findById(self, id):
        tipo_entrada = self.__repository.get_by_id(id)
        if tipo_entrada:
            return tipo_entrada
        
    def update(self, id, updated_data):
        tipo_entrada_atualizada = self.__repository.update(id, updated_data)
        return tipo_entrada_atualizada