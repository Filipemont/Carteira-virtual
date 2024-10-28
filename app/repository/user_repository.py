from model.user import User
from ext.database_ext import db


class UserRepository:
    def __init__(self):
        self.session = db.session

    def get_by_id(self, user_id):
        return self.session.query(User).filter_by(ID=user_id).first()

    def get_all(self):
        return self.session.query(User).all()

    def delete_by_id(self, user_id):
        user = self.get_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return user
        return None

    def update(self, user_id, updated_data):
        user = self.get_by_id(user_id)
        if user:
            for key, value in updated_data.items():
                setattr(user, key, value)
            self.session.commit()
            return user
        return None

    def insert(self, nome, sobrenome, email, senha, cpf):
        usuario = User(Nome=nome, Sobrenome=sobrenome, Email=email, Senha=senha, Cpf=cpf)
        self.session.add(usuario)
        self.session.commit()

    # def count(self):
    #     # Retorna a contagem total de usuários.
    #     return self.session.query(User).count()

    # def exists(self, user_id):
    #     # Verifica se um usuário existe pelo ID.
    #     return self.session.query(User).filter_by(ID=user_id).count() > 0

    def find_by_email(self, email):
        # Retorna um usuário pelo email.
        return self.session.query(User).filter_by(Email=email).first()

    # def find_by_cpf(self, cpf):
    #     # Retorna um usuário pelo CPF.
    #     return self.session.query(User).filter_by(CPF=cpf).first()
