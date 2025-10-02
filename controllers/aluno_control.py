from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from models import db
from models.aluno import Aluno
from datetime import datetime 
from helpers.date_converter import date_converter
from helpers.age_calculator import age_calculator

aluno_bp = Blueprint("aluno_bp", __name__)

@aluno_bp.route('/alunos', methods=['POST']) 
def criar_aluno():
    try:
        dados = request.get_json()
        novo_aluno = Aluno(
            nome= dados.get("nome"),
            idade= age_calculator(date_converter(dados.get("data_nascimento"))),
            turma_id= dados.get("turma_id"),
            data_nascimento= date_converter(dados.get("data_nascimento")),
            nota_primeiro_semestre= dados.get("nota_primeiro_semestre"),
            nota_segundo_semestre= dados.get("nota_segundo_semestre"),
            media_final= (dados.get("nota_primeiro_semestre") + dados.get("nota_segundo_semestre"))/2 if dados.get("nota_primeiro_semestre") is not None and dados.get("nota_segundo_semestre") is not None else None
        )
        db.session.add(novo_aluno)
        db.session.commit()

        return jsonify({"mensagem":"Aluno criado com sucesso!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"erro": "Turma não encontrada. Verifique o turma_id."}), 500


@aluno_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    lista = [
        {
            "id": aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "turma_id": aluno.turma_id,
            "data_nascimento": aluno.data_nascimento,
            "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": aluno.nota_segundo_semestre,
            "media_final": aluno.media_final
        }
        for aluno in alunos
    ]
    return jsonify({"alunos": lista, "total_alunos": len(lista)}), 200      

@aluno_bp.route('/alunos/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if aluno:
        return jsonify(
            {
                "mensagem": "Aluno encontrado com sucesso!",
                "dados_aluno": {
                    "id": aluno.id,
                    "nome": aluno.nome,
                    "idade": aluno.idade,
                    "turma_id": aluno.turma_id,
                    "data_nascimento": aluno.data_nascimento,
                    "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
                    "nota_segundo_semestre": aluno.nota_segundo_semestre,
                    "media_final": aluno.media_final
                },
            }
        ), 200
    return jsonify({"mensagem": "Aluno não encontrado."}), 404  

@aluno_bp.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualizar_aluno(id_aluno):
    dados = request.get_json()
    aluno = Aluno.query.get(id_aluno)
    if aluno:
        aluno.nome = dados.get("nome", aluno.nome)
        aluno.idade = dados.get("idade", aluno.idade)
        aluno.turma_id = dados.get("turma_id", aluno.turma_id)
        aluno.data_nascimento = dados.get("data_nascimento", aluno.data_nascimento)
        aluno.nota_primeiro_semestre = dados.get("nota_primeiro_semestre", aluno.nota_primeiro_semestre)
        aluno.nota_segundo_semestre = dados.get("nota_segundo_semestre", aluno.nota_segundo_semestre)
        aluno.media_final = dados.get("media_final", aluno.media_final)
        db.session.commit()
        return jsonify({"mensagem": "Aluno atualizado com sucesso!"}), 200
    return jsonify({"mensagem": "Aluno não encontrado."}), 404

@aluno_bp.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deletar_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if aluno:
        db.session.delete(aluno)
        db.session.commit()
        return jsonify({"mensagem": "Aluno deletado com sucesso!"}), 200
    return jsonify({"mensagem": "Aluno não encontrado."}), 404