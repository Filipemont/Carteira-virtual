from service.user_service import UserService
from flask import Blueprint, request, jsonify #type: ignore
from flasgger import swag_from #type: ignore

usuario_blueprint = Blueprint('usuario', __name__)
__user_service = UserService()


@usuario_blueprint.route('/usuarios', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de usuários retornada com sucesso',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'nome': {'type': 'string'},
                        'email': {'type': 'string'},
                        'cpf': {'type': 'string'},
                    }
                }
            }
        },
        404: {
            'description': 'Nenhum usuário encontrado na base de dados',
            'schema': {
                'type': 'object',
                'properties': {
                    'erro': {'type': 'string'}
                }
            }
        }
    }
})
def listar_usuarios():
    todos_usuarios = __user_service.find_all()
    if todos_usuarios:
        return jsonify(todos_usuarios), 200
    return jsonify({"erro": "Nenhum usuario em nossa base de dados"}), 404


@usuario_blueprint.route('/usuarios/<int:id>', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Usuário retornado com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'nome': {'type': 'string'},
                    'email': {'type': 'string'},
                }
            }
        },
        400: {
            'description': 'Usuário não encontrado',
            'schema': {
                'type': 'object',
                'properties': {
                    'erro': {'type': 'string'}
                }
            }
        }
    }
})
def obter_usuario(id):
    user = __user_service.findById(id)
    if user:
        return user
    return jsonify({"erro": "Usuario não encontrado"}), 400


@usuario_blueprint.route('/usuarios', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'sobrenome': {'type': 'string'},
                    'email': {'type': 'string'},
                    'senha': {'type': 'string'},
                    'cpf': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Usuário criado com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'mensagem': {'type': 'string'},
                    'nome': {'type': 'string'},
                    'email': {'type': 'string'}
                }
            }
        },
        400: {
            'description': 'Dados não fornecidos',
            'schema': {
                'type': 'object',
                'properties': {
                    'erro': {'type': 'string'}
                }
            }
        }
    }
})
def criar_usuario():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    usuario_nome = dados.get('nome')
    usuario_sobrenome = dados.get('sobrenome')
    usuario_email = dados.get('email')
    senha = dados.get('senha')
    cpf = dados.get('cpf')
    __user_service.save(usuario_nome, usuario_sobrenome,
                        usuario_email, senha, cpf)
    return jsonify({"mensagem": "Usuário criado", "nome": usuario_nome, "email": usuario_email}), 201


@usuario_blueprint.route('/usuarios/<int:id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'additionalProperties': True  # Aceita qualquer campo adicional
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Usuário atualizado com sucesso',
            'schema': {
                'type': 'string'
            }
        },
        400: {
            'description': 'Usuário não encontrado ou dados não fornecidos',
            'schema': {
                'type': 'object',
                'properties': {
                    'erro': {'type': 'string'}
                }
            }
        }
    }
})
def atualizar_usuario(id):
    usuario = __user_service.findById(id)
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 400
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400
    __user_service.update(id, dados)
    return f"Usuário com ID: {id} atualizado", 200


@usuario_blueprint.route('/usuarios/<int:id>', methods=['DELETE'])
@swag_from({
    'responses': {
        204: {
            'description': 'Usuário deletado com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'sucess': {'type': 'string'}
                }
            }
        },
        400: {
            'description': 'Usuário não encontrado',
            'schema': {
                'type': 'object',
                'properties': {
                    'erro': {'type': 'string'}
                }
            }
        }
    }
})
def deletar_usuario(id):
    usuario = __user_service.findById(id)
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 400
    __user_service.delete(id)
    return jsonify({"sucesso": f"Usuário com ID: {id} deletado"}), 204


@usuario_blueprint.route('/login', methods=['POST'])
@swag_from({
    'responses': {
        204: {
            'description': 'Usuário logado com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'sucess': {'type': 'string'}
                }
            }
        },
        400: {
            'description': 'Usuário não encontrado',
            'schema': {
                'type': 'object',
                'properties': {
                    'erro': {'type': 'string'}
                }
            }
        }
    }
})
def logar_usuario(email, senha):
    if not __user_service.login(email, senha) :
        return jsonify({"erro": "Usuário não encontrado"}), 400
    return jsonify({"sucesso": f"Usuário com ID: {id} logado"}), 200