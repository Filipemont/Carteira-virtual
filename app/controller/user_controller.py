from service.user_service import UserService
from flask import Blueprint, request, jsonify

usuario_blueprint = Blueprint('usuario', __name__)
__user_service = UserService()

@usuario_blueprint.route('/usuarios', methods=['GET'])
def listar_usuarios():
    todos_usuarios = __user_service.find_all()
    if todos_usuarios:   
        return jsonify(todos_usuarios),200
    return jsonify({"erro": "Nenhum usuario em nossa base de dados"}), 404

@usuario_blueprint.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuario(id):
    user = __user_service.findById(id)
    if user:
        return user
    return jsonify({"erro": "Usuario não encontrado"}), 400

@usuario_blueprint.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400
    
    usuario_nome = dados.get('nome')
    usuario_sobrenome = dados.get('sobrenome')
    usuario_email = dados.get('email')
    senha = dados.get('senha')
    cpf = dados.get('cpf')
    __user_service.save(usuario_nome, usuario_sobrenome, usuario_email, senha, cpf)
    return jsonify({"mensagem": "Usuário criado", "nome": usuario_nome, "email": usuario_email}), 201

@usuario_blueprint.route('/usuarios/<int:id>', methods=['PUT'])
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
def deletar_usuario(id):
    usuario = __user_service.findById(id)
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 400
    __user_service.delete(id)
    return f"Usuário com ID: {id} deletado", 204