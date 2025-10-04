from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from models import db
from models.turma import Turma

turma_bp = Blueprint("turma_bp", __name__)

@turma_bp.route('/turmas', methods=['POST']) 
def criar_turma():
    try:
        dados = request.get_json()
        nova_turma = Turma(
            nome= dados.get("nome"),
            professor_id= dados.get("professor_id"),
            ativo= dados.get("ativo", True)
        )
        db.session.add(nova_turma)
        db.session.commit()

        return jsonify({"mensagem":"Turma criada com sucesso!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"erro": "Professor não encontrado. Verifique o professor_id."}), 500


@turma_bp.route('/turmas', methods=['GET'])
def listar_turmas():
    turmas = Turma.query.all()
    lista = [
        {
            "id": turma.id,
            "nome": turma.nome,
            "professor_id": turma.professor_id,
            "ativo": turma.ativo
        }
        for turma in turmas
    ]
    return jsonify({"turmas": lista, "total_turmas": len(lista)}), 200

@turma_bp.route('/turmas/<int:id_turma>', methods=['GET'])
def get_turma(id_turma):
    turma = Turma.query.get(id_turma)
    if turma:
        return jsonify(
            {
                "mensagem": "Turma encontrada com sucesso!",
                "dados_turma": {
                    "id": turma.id,
                    "nome": turma.nome,
                    "professor_id": turma.professor_id,
                    "ativo": turma.ativo
                },
            }
        ), 200
    return jsonify({"mensagem": "Turma não encontrada."}), 404

@turma_bp.route('/turmas/<int:id_turma>', methods=['PUT'])
def atualizar_turma(id_turma):
    dados = request.get_json()
    turma = Turma.query.get(id_turma)
    if turma:
        turma.nome = dados.get("nome", turma.nome)
        turma.professor_id = dados.get("professor_id", turma.professor_id)
        turma.ativo = dados.get("ativo", turma.ativo)
        db.session.commit()
        return jsonify({"mensagem": "Turma atualizada com sucesso!"}), 200
    return jsonify({"mensagem": "Turma não encontrada."}), 404

@turma_bp.route('/turmas/<int:id_turma>', methods=['DELETE'])
def deletar_turma(id_turma):
    try:
        turma = Turma.query.get(id_turma)
        if not turma:
            return jsonify({"mensagem": "Turma não encontrada"}), 404
        db.session.delete(turma)
        db.session.commit()

        return jsonify({"mensagem": "Turma deletada com sucesso!"}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"mensagem": "Não é possível excluir a turma, pois ela está associada a pelo menos um aluno."}), 500



    
