from app.models.rep_utilizadores import select_nome_do_utilizador, insert_utilizador, select_todos_utilizadores
from pprint import pprint
from werkzeug.security import generate_password_hash, check_password_hash

from flask import url_for, current_app
from itsdangerous import URLSafeTimedSerializer
import logging


def listar_utilizadores():
    """Lista os utilizadores existentes 

    Returns:
        _type_: _description_
    """    
    lista_utilizadores  = select_todos_utilizadores()
    return lista_utilizadores 



def gerar_hash_password_igual_nome_u():
    lista_utilizadores  = select_todos_utilizadores()
    for utilizador in lista_utilizadores:
        print(generate_password_hash(utilizador['nome_u']))




if __name__ == "__main__":
    pprint(gerar_hash_password_igual_nome_u())