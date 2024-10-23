from model.user import User

class UserRepository:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, user_id):
        # Retorna um usuário pelo ID
        return self.session.query(User).filter_by(ID=user_id).first()

    def get_all(self):
        # Retorna todos os usuários.
        return self.session.query(User).all()

    def delete_by_id(self, user_id):
        # Deleta um usuário pelo ID e retorna o usuário deletado.
        user = self.get_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return user
        return None

    def update(self, user_id, updated_data):
        # Atualiza os dados de um usuário existente.
        user = self.get_by_id(user_id)
        if user:
            for key, value in updated_data.items():
                setattr(user, key, value)
            self.session.commit()
            return user
        return None

    def count(self):
        # Retorna a contagem total de usuários.
        return self.session.query(User).count()

    def exists(self, user_id):
        # Verifica se um usuário existe pelo ID.
        return self.session.query(User).filter_by(ID=user_id).count() > 0

    def find_by_email(self, email):
        # Retorna um usuário pelo email.
        return self.session.query(User).filter_by(Email=email).first()

    def find_by_cpf(self, cpf):
        # Retorna um usuário pelo CPF.
        return self.session.query(User).filter_by(CPF=cpf).first()
