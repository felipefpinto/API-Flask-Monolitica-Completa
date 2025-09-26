from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from . import db

class Professor(db.Model):

    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    obs = db.Column(db.String(200),default="Sem observações", nullable=False)
    
    turmas = db.relationship("Turma", back_populates="professor")



    def __repr__(self):
        return f"<Professor {self.name}>"