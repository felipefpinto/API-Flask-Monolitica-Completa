import os
from flask import Flask
from config import Config
from controllers.professor_control import professor_bp
from controllers.turma_control import turma_bp
from controllers.aluno_control import aluno_bp
from models import db
from models.professor import Professor
from models.turma import Turma
from models.aluno import Aluno
from flasgger import Swagger

app= Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(professor_bp)
app.register_blueprint(turma_bp)
app.register_blueprint(aluno_bp)

if __name__ == '__main__':
    app.run(debug=True) 
    
    