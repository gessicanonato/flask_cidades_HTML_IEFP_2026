from flask import Blueprint, request, session, redirect, url_for, flash
from app.services.srv_autenticacao import validar_login


autenticacao = Blueprint("autenticacao", __name__, url_prefix="/autenticacao") 


@autenticacao.route("/login", methods=["POST"])
def login():
    nome        = request.form.get("fuser")
    password    = request.form.get("fpass")
    resultado   = validar_login(nome, password)
    if resultado["sucesso"]:
        user                        = resultado["utilizador"]
        session["id_utilizador"]    = user["id"]
        session["nome_utilizador"]  = user["nome"]
        session["nivel_utilizador"] = user["nivel"]
        flash("Login efetuado com sucesso.", "flashSucesso")
    else:
        flash(resultado["mensagem"], "flashErro")
        
    return redirect(url_for("cidades.homepage"))


@autenticacao.route("/logout")
def logout():
    session.clear()
    flash("Sessão terminada.", "flashSucesso")
    return redirect(url_for("cidades.homepage"))


