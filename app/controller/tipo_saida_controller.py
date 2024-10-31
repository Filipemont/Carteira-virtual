from service.tipo_saida_service import TipoSaidaService
from flask import Blueprint, request, jsonify #type: ignore

tipo_saida_blueprint = Blueprint('tipo_de_saida', __name__)
__tipo_saida_service = TipoSaidaService()


@tipo_saida_blueprint.route('/tipo-de-saidas', methods=['GET'])
def listar_tipos_de_saidas():
    todas_saidas = __tipo_saida_service.find_all()
    if todas_saidas:
        return jsonify(todas_saidas), 200
    return jsonify({"erro": "Nenhum tipo de saida em nossa base de dados"}), 404


@tipo_saida_blueprint.route('/tipo-de-saidas/<int:id>', methods=['GET'])
def obter_tipos_de_saida(id):
    tipo_de_saida = __tipo_saida_service.findById(id)
    if tipo_de_saida:
        return tipo_de_saida
    return jsonify({"erro": "tipo de saida não encontrado"}), 400


@tipo_saida_blueprint.route('/tipo-de-saidas', methods=['POST'])
def criar_tipos_de_saida():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    nome = dados.get('nome')
    icone = dados.get('icone')
    __tipo_saida_service.save(nome, icone)
    return jsonify({"mensagem": "Tipo de saida criada", "Nome": nome}), 201


@tipo_saida_blueprint.route('/tipo-de-saidas/<int:id>', methods=['PUT'])
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
def deletar_tipos_de_saida(id):
    tipo_de_saida = __tipo_saida_service.findById(id)
    if not tipo_de_saida:
        return jsonify({"erro": "Tipo de saida não encontrado"}), 400
    __tipo_saida_service.delete(id)
    return jsonify({"mensagem": f"Tipo de saida com ID: {id} deletada"}), 204