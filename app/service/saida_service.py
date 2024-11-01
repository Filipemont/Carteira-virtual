from repository.saida_repository import SaidaRepository


class SaidaService:
    __repository = SaidaRepository()

    def save(self, descricao, valor, data_saida, id_tipo_saida, Id_usuario):
        self.__repository.insert(descricao, valor, data_saida, id_tipo_saida, Id_usuario)

    def find_all(self):
        return self.__repository.get_all()

    def delete(self, id):
        self.__repository.delete_by_id(id)

    def findById(self, id):
        saida = self.__repository.get_by_id(id)
        if saida:
            return saida
    
    def update(self, id, updated_data):
        saida_atualizada = self.__repository.update(id, updated_data)
        return saida_atualizada
    
    def find_by_user_id(self, user_id):
        return self.__repository.find_by_usuario_id(user_id)
    
    def find_by_tipo_saida_id(self, tipo_entrada_id):
        return self.__repository.find_by_tipo_saida(tipo_entrada_id)