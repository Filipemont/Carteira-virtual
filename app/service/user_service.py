from repository.user_repository import UserRepository
import bcrypt  # type:ignore


class UserService:
    __repository = UserRepository()

    def save(self, nome, sobrenome, email, senha, cpf):
        if not self.__repository.find_by_email(email):
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(senha.encode('utf-8'), salt)
            self.__repository.insert(nome, sobrenome, email, hashed_password, cpf, salt)

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

    def login(self, email, senha):
        usuario: object = self.__repository.find_by_email(email)
        if usuario:
            if usuario.senha == bcrypt.hashpw(senha, usuario.salt):
                return True
            else:
                return False
        return False