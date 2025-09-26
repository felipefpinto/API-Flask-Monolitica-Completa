from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from . import db

class Turma(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    nome = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    professor = db.relationship("Professor", back_populates="turmas")
    alunos = db.relationship("Aluno", back_populates="turma")
    

    

    def __repr__(self):
        return f"<Turma {self.nome} - {self.periodo}>"