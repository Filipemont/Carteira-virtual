from repository.user_repository import UserRepository
import bcrypt #type:ignore


class UserService:
    __repository = UserRepository()

    def save(self, nome, sobrenome, email, senha, cpf):
        if not self.__repository.find_by_email(email):
            salt = bcrypt.gensalt()
            self.__repository.insert(nome, sobrenome, email, senha, cpf, salt)

    def find_all(self):
        return self.__repository.get_all()

    def delete(self, id):
        self.__repository.delete_by_id(id)

    def findById(self, id):
        usuario = self.__repository.get_by_id(id)
        if usuario:
            return usuario
        
    def update(self, user_id, updated_data):
        user_atualizado = self.__repository.update(user_id, updated_data)
        return user_atualizado
    
    def find_by_email(self, email):
        return self.__repository.find_by_email(email)
