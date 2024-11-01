from repository.tipo_saida_repository import TipoSaidaRepository


class TipoSaidaService:
    __repository = TipoSaidaRepository()

    def save(self, nome, icone, id_usuario):
        self.__repository.insert(nome, icone, id_usuario)

    def find_all(self):
        return self.__repository.get_all()

    def delete(self, id):
        self.__repository.delete_by_id(id)

    def findById(self, id):
        tipo_saida = self.__repository.get_by_id(id)
        if tipo_saida:
            return tipo_saida

    def update(self, id, updated_data):
        tipo_saida_atualizada = self.__repository.update(id, updated_data)
        return tipo_saida_atualizada
    
    def find_by_user_id(self, user_id):
        return self.__repository.find_by_usuario_id(user_id)