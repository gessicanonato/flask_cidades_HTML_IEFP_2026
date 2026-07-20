from app.db_config import conectar_pymysql
from pprint import pprint

def obter_foto_por_id(id_foto, conexao=None):
    if conexao is None:
        conexao = conectar_pymysql()

    cursor = conexao.cursor()
    cursor.execute(
        "SELECT * FROM fotos WHERE id_f = %s",
        (id_foto,)
    )
    return cursor.fetchone()


def delete_foto(conexao, id_foto):
    cursor = conexao.cursor()
    cursor.execute(
        "DELETE FROM fotos WHERE id_f = %s",
        (id_foto,)
    )
    conexao.commit()


def insert_foto(novo_nome, cidade_id, desc):
    conexao = conectar_pymysql()
    cursor  = conexao.cursor()

    try:
        sql = "INSERT INTO fotos (img_f, cidade_f, desc_f) VALUES (%s, %s, %s)"
        cursor.execute(sql,(novo_nome, cidade_id, desc))
        conexao.commit()
        return True
    except Exception as e:
        conexao.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

