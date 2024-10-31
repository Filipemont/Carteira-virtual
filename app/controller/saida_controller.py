from service.saida_service import SaidaService
from flask import Blueprint, request, jsonify #type: ignore

saida_blueprint = Blueprint('saida', __name__)
__saida_service = SaidaService()


@saida_blueprint.route('/saidas', methods=['GET'])
def listar_saidas():
    todas_saidas = __saida_service.find_all()
    if todas_saidas:
        return jsonify(todas_saidas), 200
    return jsonify({"erro": "Nenhuma saida em nossa base de dados"}), 404


@saida_blueprint.route('/saidas/<int:id>', methods=['GET'])
def obter_saida(id):
    saida = __saida_service.findById(id)
    if saida:
        return saida
    return jsonify({"erro": "Saida não encontrada"}), 400


@saida_blueprint.route('/saidas', methods=['POST'])
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
def deletar_saida(id):
    saida = __saida_service.findById(id)
    if not saida:
        return jsonify({"erro": "Saida não encontrada"}), 400
    __saida_service.delete(id)
    return f"Saida com ID: {id} deletada", 204
