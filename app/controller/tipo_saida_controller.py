from service.tipo_saida_service import TipoSaidaService
from flask import Blueprint, request, jsonify #type: ignore
from flasgger import swag_from #type: ignore

tipo_saida_blueprint = Blueprint('tipo_de_saida', __name__)
__tipo_saida_service = TipoSaidaService()


@tipo_saida_blueprint.route('/tipo-de-saidas', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de todos os tipos de saída',
            'schema': {
                'type': 'array',
                'items': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'nome': {'type': 'string'}, 'icone': {'type': 'string'}}}
            }
        },
        404: {
            'description': 'Nenhum tipo de saída encontrado'
        }
    }
})
def listar_tipos_de_saidas():
    todos_tipos_de_saidas = __tipo_saida_service.find_all()
    if todos_tipos_de_saidas:
        return jsonify(todos_tipos_de_saidas), 200
    return jsonify({"erro": "Nenhum tipo de saida em nossa base de dados"}), 404


@tipo_saida_blueprint.route('/tipo-de-saidas/<int:id>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do tipo de saída'
        }
    ],
    'responses': {
        200: {
            'description': 'Tipo de saída encontrado',
            'schema': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'nome': {'type': 'string'}, 'icone': {'type': 'string'}}}
        },
        400: {
            'description': 'Tipo de saída não encontrado'
        }
    }
})
def obter_tipos_de_saida(id):
    tipo_de_saida = __tipo_saida_service.findById(id)
    if tipo_de_saida:
        return jsonify(tipo_de_saida), 200
    return jsonify({"erro": "tipo de saida não encontrado"}), 400


@tipo_saida_blueprint.route('/tipo-de-saidas-por-usuario/<int:id>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do usuário'
        }
    ],
    'responses': {
        200: {
            'description': 'Lista de tipos de saída por usuário',
            'schema': {
                'type': 'array',
                'items': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'nome': {'type': 'string'}, 'icone': {'type': 'string'}}}
            }
        },
        400: {
            'description': 'Nenhum tipo de saída encontrado para o usuário'
        }
    }
})
def obter_tipos_de_saida_por_usuario(id):
    todos_tipos_de_saidas = __tipo_saida_service.find_by_user_id(id)
    if todos_tipos_de_saidas:
        return jsonify(todos_tipos_de_saidas), 200
    return jsonify({"erro": "tipo de saida não encontrado"}), 400


@tipo_saida_blueprint.route('/tipo-de-saidas', methods=['POST'])
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
                    'icone': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Tipo de saída criado',
            'schema': {'type': 'object', 'properties': {'mensagem': {'type': 'string'}, 'Nome': {'type': 'string'}}}
        },
        400: {
            'description': 'Dados não fornecidos'
        }
    }
})
def criar_tipos_de_saida():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    nome = dados.get('nome')
    icone = dados.get('icone')
    __tipo_saida_service.save(nome, icone)
    return jsonify({"mensagem": "Tipo de saida criada", "Nome": nome}), 201


@tipo_saida_blueprint.route('/tipo-de-saidas/<int:id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do tipo de saída a ser atualizado'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'icone': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Tipo de saída atualizado com sucesso'
        },
        400: {
            'description': 'Tipo de saída não encontrado ou dados não fornecidos'
        }
    }
})
def atualizar_tipos_de_saida(id):
    tipo_de_saida = __tipo_saida_service.findById(id)
    if not tipo_de_saida:
        return jsonify({"erro": "Tipo de saida não encontrada"}), 400
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400
    __tipo_saida_service.update(id, dados)
    return f"Tipo de saida com ID: {id} atualizada", 200


@tipo_saida_blueprint.route('/tipo-de-saidas/<int:id>', methods=['DELETE'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do tipo de saída a ser deletado'
        }
    ],
    'responses': {
        204: {
            'description': 'Tipo de saída deletada com sucesso'
        },
        400: {
            'description': 'Tipo de saída não encontrado'
        }
    }
})
def deletar_tipos_de_saida(id):
    tipo_de_saida = __tipo_saida_service.findById(id)
    if not tipo_de_saida:
        return jsonify({"erro": "Tipo de saida não encontrado"}), 400
    __tipo_saida_service.delete(id)
    return jsonify({"mensagem": f"Tipo de saida com ID: {id} deletada"}), 204