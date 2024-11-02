from service.entrada_service import EntradaService
from flask import Blueprint, request, jsonify  # type: ignore
from flasgger import swag_from  # type: ignore

entrada_blueprint = Blueprint('entrada', __name__)
__entrada_service = EntradaService()


@entrada_blueprint.route('/entradas', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de todas as entradas',
            'schema': {
                'type': 'array',
                'items': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'Descricao': {'type': 'string'}, 'Valor': {'type': 'number'}, 'DataEntrada': {'type': 'string'}, 'ID_Tipo_Entrada': {'type': 'integer'}, 'ID_Usuario': {'type': 'integer'}}}
            }
        },
        404: {
            'description': 'Nenhuma entrada encontrada'
        }
    }
})
def listar_entradas():
    todas_entradas = __entrada_service.find_all()
    if todas_entradas:
        return jsonify(todas_entradas), 200
    return jsonify({"erro": "Nenhum usuario em nossa base de dados"}), 404


@entrada_blueprint.route('/entradas-por-usuario/<int:id>', methods=['GET'])
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
            'description': 'Lista de entradas para o usuário',
            'schema': {
                'type': 'array',
                'items': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'Descricao': {'type': 'string'}, 'Valor': {'type': 'number'}, 'DataEntrada': {'type': 'string'}, 'ID_Tipo_Entrada': {'type': 'integer'}, 'ID_Usuario': {'type': 'integer'}}}
            }
        },
        400: {
            'description': 'Usuário não encontrado'
        }
    }
})
def obter_entrada_por_usuario(id):
    entradas = __entrada_service.find_by_usuario_id(id)
    if entradas:
        return jsonify(entradas), 200
    return jsonify({"erro": "Usuario não encontrado"}), 400


@entrada_blueprint.route('/entradas-por-tipo-entrada/<int:id>', methods=['GET'])
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
            'description': 'Lista de entradas para o tipo de entrada',
            'schema': {
                'type': 'array',
                'items': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'Descricao': {'type': 'string'}, 'Valor': {'type': 'number'}, 'DataEntrada': {'type': 'string'}, 'ID_Tipo_Entrada': {'type': 'integer'}, 'ID_Usuario': {'type': 'integer'}}}
            }
        },
        400: {
            'description': 'Tipo de entrada não encontrado'
        }
    }
})
def obter_entrada_por_tipo_entrada(id):
    entradas = __entrada_service.find_by_tipo_entrada_id(id)
    if entradas:
        return jsonify(entradas), 200
    return jsonify({"erro": "Usuario não encontrado"}), 400


@entrada_blueprint.route('/entradas/<int:id>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da entrada'
        }
    ],
    'responses': {
        200: {
            'description': 'Entrada encontrada',
            'schema': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'Descricao': {'type': 'string'}, 'Valor': {'type': 'number'}, 'DataEntrada': {'type': 'string'}, 'ID_Tipo_Entrada': {'type': 'integer'}, 'ID_Usuario': {'type': 'integer'}}}
        },
        400: {
            'description': 'Entrada não encontrada'
        }
    }
})
def obter_entrada(id):
    entrada = __entrada_service.findById(id)
    if entrada:
        return entrada
    return jsonify({"erro": "Usuario não encontrado"}), 400


@entrada_blueprint.route('/entradas', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'Descricao': {'type': 'string'},
                    'Valor': {'type': 'number'},
                    'DataEntrada': {'type': 'string', 'format': 'date'},
                    'id_tipo_entrada': {'type': 'integer'},
                    'id_usuario': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Entrada criada',
            'schema': {'type': 'object', 'properties': {'mensagem': {'type': 'string'}, 'Descrição': {'type': 'string'}, 'Valor': {'type': 'number'}}}
        },
        400: {
            'description': 'Dados não fornecidos'
        }
    }
})
def criar_entrada():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    Descricao = dados.get('Descricao')
    Valor = dados.get('Valor')
    DataEntrada = dados.get('DataEntrada')
    ID_Tipo_Entrada = dados.get('id_tipo_entrada')
    ID_Usuario = dados.get('id_usuario')
    __entrada_service.save(Descricao, Valor,
                           DataEntrada, ID_Tipo_Entrada, ID_Usuario)
    return jsonify({"mensagem": "Entrada criada", "Descrição": Descricao, "Valor": Valor}), 201


@entrada_blueprint.route('/entradas/<int:id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da entrada a ser atualizada'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'Descricao': {'type': 'string'},
                    'Valor': {'type': 'number'},
                    'DataEntrada': {'type': 'string', 'format': 'date'},
                    'ID_Tipo_Entrada': {'type': 'integer'},
                    'ID_Usuario': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Entrada atualizada com sucesso'
        },
        400: {
            'description': 'Entrada não encontrada ou dados não fornecidos'
        }
    }
})
def atualizar_entrada(id):
    entrada = __entrada_service.findById(id)
    if not entrada:
        return jsonify({"erro": "Entrada não encontrada"}), 400
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400
    __entrada_service.update(id, dados)
    return f"Entrada com ID: {id} atualizada", 200


@entrada_blueprint.route('/entradas/<int:id>', methods=['DELETE'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da entrada a ser deletada'
        },
    ],
    'responses': {
        204: {
            'description': 'Entrada deletada com sucesso'
        },
        400: {
            'description': 'Entrada não encontrada'
        }
    }
})
def deletar_entrada(id):
    entrada = __entrada_service.findById(id)
    if not entrada:
        return jsonify({"erro": "Entrada não encontrado"}), 400
    __entrada_service.delete(id)
    return f"Entrada com ID: {id} deletada", 204
