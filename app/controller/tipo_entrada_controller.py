from service.tipo_entrada_service import TipoEntradaService
from flask import Blueprint, request, jsonify #type: ignore
from flasgger import swag_from # type: ignore

tipo_entrada_blueprint = Blueprint('tipo_de_entrada', __name__)
__tipo_entrada_service = TipoEntradaService()


@tipo_entrada_blueprint.route('/tipo-de-entradas', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de todos os tipos de entrada',
            'schema': {
                'type': 'array',
                'items': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'nome': {'type': 'string'}, 'icone': {'type': 'string'}}}
            }
        },
        404: {
            'description': 'Nenhum tipo de entrada encontrado'
        }
    }
})
def listar_tipos_de_entradas():
    todas_entradas = __tipo_entrada_service.find_all()
    if todas_entradas:
        return jsonify(todas_entradas), 200
    return jsonify({"erro": "Nenhum tipo de entrada em nossa base de dados"}), 404

@tipo_entrada_blueprint.route('/tipo-de-entradas/<int:id>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do tipo de entrada'
        }
    ],
    'responses': {
        200: {
            'description': 'Tipo de entrada encontrado',
            'schema': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'nome': {'type': 'string'}, 'icone': {'type': 'string'}}}
        },
        400: {
            'description': 'Tipo de entrada não encontrado'
        }
    }
})
def obter_tipos_de_entrada(id):
    tipo_de_entrada = __tipo_entrada_service.findById(id)
    if tipo_de_entrada:
        return jsonify(tipo_de_entrada), 200
    return jsonify({"erro": "tipo de entrada não encontrado"}), 400

@tipo_entrada_blueprint.route('/tipo-de-entradas-por-usuario/<int:id>', methods=['GET'])
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
            'description': 'Lista de tipos de entrada por usuário',
            'schema': {
                'type': 'array',
                'items': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'nome': {'type': 'string'}, 'icone': {'type': 'string'}}}
            }
        },
        404: {
            'description': 'Nenhum tipo de entrada encontrado para o usuário'
        }
    }
})
def obter_tipos_de_entrada_por_usuario(id):
    todas_entradas = __tipo_entrada_service.find_by_user_id(id)
    if todas_entradas:
        return jsonify(todas_entradas), 200
    return jsonify({"erro": "Nenhum tipo de entrada em nossa base de dados"}), 404

@tipo_entrada_blueprint.route('/tipo-de-entradas', methods=['POST'])
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
                    'icone': {'type': 'string'},
                    'id_usuario': {'type': 'integer'},
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Tipo de entrada criado',
            'schema': {'type': 'object', 'properties': {'mensagem': {'type': 'string'}, 'Nome': {'type': 'string'}}}
        },
        400: {
            'description': 'Dados não fornecidos'
        }
    }
})
def criar_tipos_de_entrada():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    nome = dados.get('nome')
    icone = dados.get('icone')
    id_usuario = dados.get('id_usuario')
    __tipo_entrada_service.save(nome, icone, id_usuario)
    return jsonify({"mensagem": "Tipo de entrada criada", "Nome": nome}), 201


@tipo_entrada_blueprint.route('/tipo-de-entradas/<int:id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do tipo de entrada a ser atualizado'
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
            'description': 'Tipo de entrada atualizado com sucesso'
        },
        400: {
            'description': 'Tipo de entrada não encontrado ou dados não fornecidos'
        }
    }
})
def atualizar_tipos_de_entrada(id):
    tipo_de_entrada = __tipo_entrada_service.findById(id)
    if not tipo_de_entrada:
        return jsonify({"erro": "Tipo de entrada não encontrada"}), 400
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400
    __tipo_entrada_service.update(id, dados)
    return f"Tipo de entrada com ID: {id} atualizada", 200


@tipo_entrada_blueprint.route('/tipo-de-entradas/<int:id>', methods=['DELETE'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do tipo de entrada a ser deletado'
        }
    ],
    'responses': {
        204: {
            'description': 'Tipo de entrada deletada com sucesso'
        },
        400: {
            'description': 'Tipo de entrada não encontrado'
        }
    }
})
def deletar_tipos_de_entrada(id):
    tipo_de_entrada = __tipo_entrada_service.findById(id)
    if not tipo_de_entrada:
        return jsonify({"erro": "Tipo de entrada não encontrado"}), 400
    __tipo_entrada_service.delete(id)
    return jsonify({"mensagem": f"Tipo de entrada com ID: {id} deletada"}), 204