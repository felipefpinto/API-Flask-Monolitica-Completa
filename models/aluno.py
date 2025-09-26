from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from . import db

class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)    
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=True)
    nota_primeiro_semestre = db.Column(db.Float, nullable=True)
    nota_segundo_semestre = db.Column(db.Float, nullable=True)
    media_final = db.Column(db.Float, nullable=True)

    turma = db.relationship("Turma", back_populates="alunos")



    def __repr__(self):
        return f"<Aluno {self.nome} - {self.turma.nome}>" 