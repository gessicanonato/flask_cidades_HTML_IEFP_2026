from functools import wraps
from flask import session, redirect, url_for, flash


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "id_utilizador" not in session:
            flash("A página que tentou aceder é protegida.", "flashErro")
            return redirect(url_for("cidades.homepage"))  # homepage
        return view(*args, **kwargs)
    return wrapped_view



def login_nivel_1_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "id_utilizador" not in session:
            flash("A página que tentou aceder é protegida.", "flashErro")
            return redirect(url_for("cidades.homepage"))  # homepage
        elif session['nivel_utilizador'] != 1:
            flash("O seu login não permite acesso a esta página.", "flashErro")
            return redirect(url_for("cidades.homepage"))  # homepage
        return view(*args, **kwargs)
    return wrapped_view


"""
def login_required(view):                       
    @wraps(view)                               
    def wrapped_view(*args, **kwargs):
        if "id_utilizador" not in session:
            flash("A página que tentou aceder é protegida.", "flashErro")
            return redirect(url_for("cidades.homepage"))  # homepage
        return view(*args, **kwargs)
    return wrapped_view

"""
# def login_required(view):   view é a função original da rota (ex: eliminar = login_required(eliminar)
# @wraps(view) Este decorador vem de: "from functools import wraps" e serve para preservar os metadados da função original. É praticamente obrigatório sempre que se cria um decorador.
# def wrapped_view(*args, **kwargs): Esta é a função que vai substituir a original. É ela que é executada. Usa (*args, **kwargs) porque não sabemos como será a função original. def editar(id): recebe um argumento; def editar(id, categoria): recebe dois. Usando (*args, **kwargs) o decorador funciona para qualquer função.
# if "id_utilizador" not in session: se o dicionário session não tiver a chave "id_utilizador"
# RESUMINDO: se o login estiver feito retorna a função original (ex:eliminar) senão retorna a mesnsagem flash e o redirecionamento previsto para logins não feitos