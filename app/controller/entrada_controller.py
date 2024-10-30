from service.entrada_service import EntradaService
from flask import Blueprint, request, jsonify #type: ignore

entrada_blueprint = Blueprint('entrada', __name__)
__entrada_service = EntradaService()


@entrada_blueprint.route('/entradas', methods=['GET'])
def listar_entradas():
    todas_entradas = __entrada_service.find_all()
    if todas_entradas:
        return jsonify(todas_entradas), 200
    return jsonify({"erro": "Nenhum usuario em nossa base de dados"}), 404


@entrada_blueprint.route('/entradas/<int:id>', methods=['GET'])
def obter_entrada(id):
    entrada = __entrada_service.findById(id)
    if entrada:
        return entrada
    return jsonify({"erro": "Usuario não encontrado"}), 400


@entrada_blueprint.route('/entradas', methods=['POST'])
def criar_entrada():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    Descricao = dados.get('Descricao')
    Valor = dados.get('Valor')
    DataEntrada = dados.get('DataEntrada')
    ID_Tipo_Entrada = dados.get('senha')
    ID_Usuario = dados.get('cpf')
    __entrada_service.save(Descricao, Valor,
                           DataEntrada, ID_Tipo_Entrada, ID_Usuario)
    return jsonify({"mensagem": "Entrada criada", "Descrição": Descricao, "Valor": Valor}), 201


@entrada_blueprint.route('/entradas/<int:id>', methods=['PUT'])
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
def deletar_entrada(id):
    entrada = __entrada_service.findById(id)
    if not entrada:
        return jsonify({"erro": "Entrada não encontrado"}), 400
    __entrada_service.delete(id)
    return f"Entrada com ID: {id} deletada", 204
