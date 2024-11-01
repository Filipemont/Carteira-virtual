from service.saida_service import SaidaService
from flask import Blueprint, request, jsonify #type: ignore
from flasgger import swag_from # type: ignore

saida_blueprint = Blueprint('saida', __name__)
__saida_service = SaidaService()


@saida_blueprint.route('/saidas', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de todas as saídas',
            'schema': {
                'type': 'array',
                'items': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'Descricao': {'type': 'string'}, 'Valor': {'type': 'number'}, 'DataSaida': {'type': 'string'}, 'ID_Tipo_Saida': {'type': 'integer'}, 'ID_Usuario': {'type': 'integer'}}}
            }
        },
        404: {
            'description': 'Nenhuma saída encontrada'
        }
    }
})
def listar_saidas():
    todas_saidas = __saida_service.find_all()
    if todas_saidas:
        return jsonify(todas_saidas), 200
    return jsonify({"erro": "Nenhuma saida em nossa base de dados"}), 404

@saida_blueprint.route('/saidas-por-usuario/<int:id>', methods=['GET'])
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
            'description': 'Lista de saídas por usuário',
            'schema': {
                'type': 'array',
                'items': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'Descricao': {'type': 'string'}, 'Valor': {'type': 'number'}, 'DataSaida': {'type': 'string'}, 'ID_Tipo_Saida': {'type': 'integer'}, 'ID_Usuario': {'type': 'integer'}}}
            }
        },
        404: {
            'description': 'Nenhuma saída encontrada para o usuário'
        }
    }
})
def listar_saidas_por_usuario(id):
    todas_saidas = __saida_service.find_by_user_id(id)
    if todas_saidas:
        return jsonify(todas_saidas), 200
    return jsonify({"erro": "Nenhuma saida em nossa base de dados"}), 404

@saida_blueprint.route('/saidas-por-tipo-saida/<int:id>', methods=['GET'])
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
            'description': 'Lista de saídas por tipo de saída',
            'schema': {
                'type': 'array',
                'items': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'Descricao': {'type': 'string'}, 'Valor': {'type': 'number'}, 'DataSaida': {'type': 'string'}, 'ID_Tipo_Saida': {'type': 'integer'}, 'ID_Usuario': {'type': 'integer'}}}
            }
        },
        404: {
            'description': 'Nenhuma saída encontrada para o tipo de saída'
        }
    }
})
def listar_saidas_por_tipo_saida(id):
    todas_saidas = __saida_service.find_by_tipo_saida_id(id)
    if todas_saidas:
        return jsonify(todas_saidas), 200
    return jsonify({"erro": "Nenhuma saida em nossa base de dados"}), 404

@saida_blueprint.route('/saidas/<int:id>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da saída'
        }
    ],
    'responses': {
        200: {
            'description': 'Saída encontrada',
            'schema': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'Descricao': {'type': 'string'}, 'Valor': {'type': 'number'}, 'DataSaida': {'type': 'string'}, 'ID_Tipo_Saida': {'type': 'integer'}, 'ID_Usuario': {'type': 'integer'}}}
        },
        400: {
            'description': 'Saída não encontrada'
        }
    }
})
def obter_saida(id):
    saida = __saida_service.findById(id)
    if saida:
        return saida
    return jsonify({"erro": "Saida não encontrada"}), 400


@saida_blueprint.route('/saidas', methods=['POST'])
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
                    'DataSaida': {'type': 'string', 'format': 'date'},
                    'ID_Tipo_Saida': {'type': 'integer'},
                    'ID_Usuario': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Saída criada',
            'schema': {'type': 'object', 'properties': {'mensagem': {'type': 'string'}, 'Descrição': {'type': 'string'}, 'Valor': {'type': 'number'}}}
        },
        400: {
            'description': 'Dados não fornecidos'
        }
    }
})
def criar_saida():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    Descricao = dados.get('Descricao')
    Valor = dados.get('Valor')
    DataSaida = dados.get('DataSaida')
    ID_Tipo_Saida = dados.get('senha')
    ID_Usuario = dados.get('cpf')
    __saida_service.save(Descricao, Valor,
                           DataSaida, ID_Tipo_Saida, ID_Usuario)
    return jsonify({"mensagem": "Saida criada", "Descrição": Descricao, "Valor": Valor}), 201


@saida_blueprint.route('/saidas/<int:id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da saída a ser atualizada'
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
                    'DataSaida': {'type': 'string', 'format': 'date'},
                    'ID_Tipo_Saida': {'type': 'integer'},
                    'ID_Usuario': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Saída atualizada com sucesso'
        },
        400: {
            'description': 'Saída não encontrada ou dados não fornecidos'
        }
    }
})
def atualizar_saida(id):
    saida = __saida_service.findById(id)
    if not saida:
        return jsonify({"erro": "Saida não encontrada"}), 400
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400
    __saida_service.update(id, dados)
    return f"Saida com ID: {id} atualizada", 200


@saida_blueprint.route('/saidas/<int:id>', methods=['DELETE'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da saída a ser deletada'
        }
    ],
    'responses': {
        204: {
            'description': 'Saída deletada com sucesso'
        },
        400: {
            'description': 'Saída não encontrada'
        }
    }
})
def deletar_saida(id):
    saida = __saida_service.findById(id)
    if not saida:
        return jsonify({"erro": "Saida não encontrada"}), 400
    __saida_service.delete(id)
    return f"Saida com ID: {id} deletada", 204
