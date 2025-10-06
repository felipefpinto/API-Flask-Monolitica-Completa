import os
from flask import Flask,redirect, Blueprint,url_for
from config import Config
from controllers.professor_control import professor_bp
from controllers.turma_control import turma_bp
from controllers.aluno_control import aluno_bp
from models import db
from models.professor import Professor
from models.turma import Turma
from models.aluno import Aluno
from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint
SWAGGER_URL = '/swagger'
API_URL = '/static/doc/doc_swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'API Monolítica em Flask',
        'uicolor': '#1a1a1a',
        'docExpansion': 'list',
        'tryItOutEnabled': True, 
        'filter': True,
        'displayOperationId': True,
        'requestSnippetsEnabled': True, 
        'supportedSubmitMethods': ['get', 'post', 'put', 'delete']
    }
)
app= Flask(__name__)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(professor_bp)
app.register_blueprint(turma_bp)
app.register_blueprint(aluno_bp)

@app.route('/')
def index():
    return redirect('/swagger')


if __name__ == '__main__':
    app.run(debug=True) 
    
    