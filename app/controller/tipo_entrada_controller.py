from service.tipo_entrada_service import TipoEntradaService
from flask import Blueprint, request, jsonify #type: ignore

tipo_entrada_blueprint = Blueprint('tipo_de_entrada', __name__)
__tipo_entrada_service = TipoEntradaService()


@tipo_entrada_blueprint.route('/tipo-de-entradas', methods=['GET'])
def listar_tipos_de_entradas():
    todas_entradas = __tipo_entrada_service.find_all()
    if todas_entradas:
        return jsonify(todas_entradas), 200
    return jsonify({"erro": "Nenhum tipo de entrada em nossa base de dados"}), 404


@tipo_entrada_blueprint.route('/tipo-de-entradas/<int:id>', methods=['GET'])
def obter_tipos_de_entrada(id):
    tipo_de_entrada = __tipo_entrada_service.findById(id)
    if tipo_de_entrada:
        return tipo_de_entrada
    return jsonify({"erro": "tipo de entrada não encontrado"}), 400


@tipo_entrada_blueprint.route('/tipo-de-entradas', methods=['POST'])
def criar_tipos_de_entrada():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    nome = dados.get('nome')
    icone = dados.get('icone')
    __tipo_entrada_service.save(nome, icone)
    return jsonify({"mensagem": "Tipo de entrada criada", "Nome": nome}), 201


@tipo_entrada_blueprint.route('/tipo-de-entradas/<int:id>', methods=['PUT'])
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
def deletar_tipos_de_entrada(id):
    tipo_de_entrada = __tipo_entrada_service.findById(id)
    if not tipo_de_entrada:
        return jsonify({"erro": "Tipo de entrada não encontrado"}), 400
    __tipo_entrada_service.delete(id)
    return jsonify({"mensagem": f"Tipo de entrada com ID: {id} deletada"}), 204