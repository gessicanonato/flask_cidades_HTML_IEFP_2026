import os
import time

from app.db_config import conectar_pymysql
from app.models.rep_fotos import  obter_foto_por_id, insert_foto, delete_foto
from werkzeug.utils import secure_filename


def eliminar_fotografia(id_foto):
    conexao = conectar_pymysql()
    foto = obter_foto_por_id(id_foto, conexao)

    if not foto:
        return False, "Fotografia não encontrada"

    caminho = os.path.join(
        "static",
        "img",
        "cidades",
        foto["img_f"]
    )

    try:
        if os.path.exists(caminho):
            os.remove(caminho)

        delete_foto(conexao, id_foto)

        return True, "Fotografia eliminada com sucesso"

    except Exception:
        return False, "Erro ao eliminar a fotografia"

    finally:
        conexao.close()


def descobrir_cidade_pela_foto(id_foto):
    resultado = obter_foto_por_id(id_foto)
    cidade = resultado["cidade_f"]
    return cidade




UPLOAD_FOLDER = "app/static/img/cidades"

def adicionar_foto_service(foto, cidade_id, desc):

    if not foto:
        return False

    # obter extensão do ficheiro
    extensao = foto.filename.rsplit(".", 1)[1].lower()

    # equivalente ao microtime(true) do PHP
    novo_nome = f"{int(time.time()*1000)}.{extensao}"

    caminho = os.path.join(UPLOAD_FOLDER, novo_nome)

    # guardar o ficheiro
    foto.save(caminho)

    # guardar na BD
    return insert_foto(novo_nome, cidade_id, desc)
