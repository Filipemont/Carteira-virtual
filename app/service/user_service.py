from repository.user_repository import UserRepository


class UserService:
    __repository = UserRepository()

    def save(self, nome, sobrenome, email, senha, cpf):
        if not self.__repository.find_by_email(email):
            self.__repository.insert(nome, sobrenome, email, senha, cpf)

    def find_all(self):
        return self.__repository.get_all()

    def delete(self, id):
        self.__repository.delete_by_id(id)

    def findById(self, id):
        usuario = self.__repository.get_by_id(id)
        if usuario:
            return usuario
