from repository.tipo_entrada_repository import TipoEntradaRepository


class TipoEntradaService:
    __repository = TipoEntradaRepository()

    def save(self, nome, icone, id_usuario):
        self.__repository.insert(nome, icone, id_usuario)

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
    
    def find_by_user_id(self, user_id):
        return self.__repository.find_by_usuario_id(user_id)
    