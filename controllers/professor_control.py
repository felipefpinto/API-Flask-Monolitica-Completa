from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from models import db
from models.professor import Professor

professor_bp = Blueprint("professor_bp", __name__)

# Criar professor
@professor_bp.route("/professores", methods=["POST"])
def criar_professor():
    dados = request.get_json()

    novo_professor = Professor(
        nome=dados.get("nome"),
        idade=dados.get("idade"),
        materia=dados.get("materia"),
        obs=dados.get("obs"),
    )

    db.session.add(novo_professor)
    db.session.commit()

    return jsonify({"mensagem":"Professor criado com sucesso!"}), 201


# Listar todos os professores
@professor_bp.route("/professores", methods=["GET"])
def get_professores():
    professores = Professor.query.all()

    lista = [
        {
            "id": prof.id,
            "nome": prof.nome,
            "idade": prof.idade,
            "materia": prof.materia,
            "obs": prof.obs,
        }
        for prof in professores
    ]

    return jsonify({"professores": lista, "total_professores": len(lista)}), 200


# Buscar professor por ID
@professor_bp.route("/professores/<int:id_professor>", methods=["GET"])
def get_professor(id_professor):
    professor = Professor.query.get(id_professor)
    if professor:
        return jsonify(
            {
                "mensagem": "Professor encontrado com sucesso!",
                "dados_professor": {
                    "id": professor.id,
                    "nome": professor.nome,
                    "idade": professor.idade,
                    "materia": professor.materia,
                    "obs": professor.obs,
                },
            }
        ), 200

    return jsonify({"mensagem": "Professor não encontrado"}), 404


# Atualizar professor
@professor_bp.route("/professores/<int:id_professor>", methods=["PUT"])
def update_professor(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        return jsonify({"mensagem": "Professor não encontrado"}), 404

    dados = request.get_json()
    professor.nome = dados.get("nome", professor.nome)
    professor.idade = dados.get("idade", professor.idade)
    professor.materia = dados.get("materia", professor.materia)
    professor.obs = dados.get("obs", professor.obs)

    db.session.commit()

    return jsonify({"mensagem": "Dados do professor atualizados com sucesso!"})


# Deletar professor
@professor_bp.route("/professores/<int:id_professor>", methods=["DELETE"])
def delete_professor(id_professor):
    try:
        professor = Professor.query.get(id_professor)
        if not professor:
            return jsonify({"mensagem": "Professor não encontrado"}), 404

        db.session.delete(professor)
        db.session.commit()

        return jsonify({"mensagem": "Professor excluído com sucesso"})
    except IntegrityError:
        db.session.rollback()
        return jsonify({"mensagem": "Não é possível excluir o professor, pois ele está associado a uma turma."}), 500
