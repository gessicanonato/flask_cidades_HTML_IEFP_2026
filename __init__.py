from flask import Flask, session   # classe usada para instanciar a aplicação web
from datetime import datetime
import os


def criar_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SK', 'dev-inseguro')


    # context_processor é uma função de injeção de variáveis para templates Jinja.
    # é executado APENAS quando um template é renderizado
    @app.context_processor
    def inject_vars():
        return {
            "user_logado"   : session.get("id_utilizador"),
            "username"      : session.get("nome_utilizador"),
            "user_nivel"    : session.get("nivel_utilizador"),
            "data_atual"    : datetime.now()
        }


    # importar blueprints 
    from app.routes.rt_cidades import cidades
    from app.routes.rt_autenticacao import autenticacao

    # registar blueprints
    app.register_blueprint(cidades)
    app.register_blueprint(autenticacao)

    return app
















    """    
    # context_processor é uma função de injeção de variáveis para templates Jinja.
    # é executado APENAS quando um template é renderizado
    @app.context_processor
    def inject_vars():
        return {
            "user_logado"   : session.get("id_utilizador"),
            "username"      : session.get("nome_utilizador"),
            "data_atual"    : datetime.now()
        }
    """