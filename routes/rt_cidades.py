from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.srv_cidades import lista_cidades, detalhes_cidade, adicionar_cidade, atualizar_cidade, eliminar_cidade, pesquisa_cidades
from app.services.srv_fotos import eliminar_fotografia, descobrir_cidade_pela_foto, adicionar_foto_service
from app.utils.decorators import login_required, login_nivel_1_required
# from pprint import pprint


# cidades = Blueprint('cidades', __name__, url_prefix="/cidades")
cidades = Blueprint('cidades', __name__)


@cidades.route("/")
def homepage():
    dados = lista_cidades()
    return render_template("home.html", lista_cidades=dados)


@cidades.route("/detalhes/<int:cidade_id>")
def detalhes(cidade_id):
    detalhes = detalhes_cidade(cidade_id)
    return render_template("detalhes.html",dados=detalhes)


@cidades.route("/adicionar", methods=["GET","POST"])
@login_required
def add_cidade():
    if request.method == "POST":
        nome        = request.form.get("fnome")
        pais        = request.form.get("fpais")
        dataf       = request.form.get("fdataf")
        habitantes  = request.form.get("fhabitantes")
        desc        = request.form.get("fdescricao")
        cidade_nova = adicionar_cidade(nome, dataf, pais, habitantes, desc)
        
        if cidade_nova:
            flash("Cidade adicionada com sucesso","flashSucesso")
            return redirect(url_for("cidades.homepage"))
        else:
            flash("Erro ao adicionar cidade","flashErro")
            return redirect(url_for("cidades.add_cidade"))

    #elif request.method == "GET":
    else:
        return render_template("adicionar.html")


@cidades.route("/listar")
@login_required
def lista_atualizar():
    dados = lista_cidades()
    return render_template("atualizar_1.html", cidades=dados)


@cidades.route("/atualizar/<int:cidade_id>", methods=["GET","POST"])
@login_required
def editar_atualizar(cidade_id):
    if request.method == "POST":
        nome        = request.form.get("fnome")
        pais        = request.form.get("fpais")
        dataf       = request.form.get("fdataf")
        habitantes  = request.form.get("fhabitantes")
        desc        = request.form.get("fdescricao")

        cidade_atualizada = atualizar_cidade(cidade_id, nome, dataf, pais, habitantes, desc)
        if cidade_atualizada:
            flash("Cidade atualizada com sucesso","flashSucesso")
            return redirect(url_for("cidades.homepage"))
        else:
            flash("Erro ao atualizar cidade","flashErro")
            return redirect(url_for('cidades.editar_atualizar',cidade_id=cidade_id))
    else:
        detalhes = detalhes_cidade(cidade_id)  # detalhes é uma lista 
        # detalhes[0] são os dados
        # detalhes[1] são as fotografias
        return(render_template("atualizar_2.html",dados=detalhes[0]))



@cidades.route("/eliminar")
@login_nivel_1_required
def lista_eliminar():
    dados = lista_cidades()
    return render_template("eliminar.html", cidades=dados)


@cidades.route("/eliminar_2/<int:cidade_id>")
@login_nivel_1_required
def del_cidade(cidade_id):
    cidade_eliminada = eliminar_cidade(cidade_id)
    if cidade_eliminada:
        flash("Cidade eliminada com sucesso","flashSucesso")
        return redirect(url_for("cidades.homepage"))
    else:
        flash("Erro ao eliminar cidade","flashErro")
        return redirect(url_for('cidades.lista_eliminar'))


@cidades.route("/pesquisa", methods=["POST"])
def pesquisa():
    string_pesquisada = request.form.get('fpesquisa')
    str_pesquisada, dados_pesquisados = pesquisa_cidades(string_pesquisada)
    return render_template("pesquisa.html", str=str_pesquisada, dados= dados_pesquisados)

@cidades.route("/eliminar_foto/<int:id_foto>")
@login_nivel_1_required
def eliminar_foto(id_foto):
    cidade = descobrir_cidade_pela_foto(id_foto)
    resultado, mensagem = eliminar_fotografia(id_foto)

    if resultado:
        flash(mensagem,"flashSucesso")
        return redirect(url_for('cidades.detalhes', cidade_id=cidade))
    else:
        flash(mensagem,"flashErro")
        return redirect(url_for('cidades.detalhes', cidade_id=cidade))



@cidades.route("/adicionar_foto", methods=["GET","POST"])
@login_nivel_1_required
def adicionar_foto():
    if request.method == "POST":
        foto = request.files.get("ffoto")
        cidade_id = request.form.get("fcidade")
        desc = request.form.get("fdesc", "")

        resultado = adicionar_foto_service(foto, cidade_id, desc)
        if resultado:
            flash("Fotografia adicionada","flashSucesso")
            return redirect(url_for("cidades.adicionar_foto"))  
        else:
            flash("A fotografia não foi adicionada","flashErro")
            return redirect(url_for("cidades.adicionar_foto")) 

    else:
        dados = lista_cidades()
        return render_template("ad_foto.html", cidades = dados)
