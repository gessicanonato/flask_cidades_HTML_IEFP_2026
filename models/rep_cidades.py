from app.db_config import conectar_pymysql
from pprint import pprint

def select_todas_cidades():
    conexao = conectar_pymysql()
    cursor = conexao.cursor()

    sql = "SELECT * FROM cidades"
    cursor.execute(sql)
    resultado = cursor.fetchall()

    return(resultado)



def select_cidade(cidade_id):
    conexao = conectar_pymysql()
    cursor = conexao.cursor()

    sql = "SELECT * FROM cidades WHERE id_c = %s"
    cursor.execute(sql,(cidade_id,))
    resultado = cursor.fetchone()

    return(resultado)



def select_imagens_cidade(cidade_id):
    conexao = conectar_pymysql()
    cursor = conexao.cursor()

    sql = "SELECT img_f, id_f FROM fotos WHERE cidade_f = %s"
    cursor.execute(sql,(cidade_id,))
    resultado = cursor.fetchall()

    return(resultado)



def insert_into_cidade(nome, dataf, pais, habitantes, desc):
    conexao = conectar_pymysql()
    cursor = conexao.cursor()

    try:
        sql = "INSERT INTO cidades (nome_c, dataf_c, pais_c, habitantes_c, desc_c) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql,(nome, dataf, pais, habitantes, desc))
        conexao.commit()
        return True
    except Exception as e:
        print(e)
        conexao.rollback()
        return False
        


def update_cidade(id, nome, dataf, pais, habitantes, desc):
    conexao = conectar_pymysql()
    cursor = conexao.cursor()

    try:
        sql = "UPDATE cidades SET nome_c=%s, dataf_c=%s, pais_c=%s, habitantes_c=%s, desc_c=%s WHERE id_c=%s"
        cursor.execute(sql,(nome, dataf, pais, habitantes, desc, id))
        conexao.commit()
        return True
    except Exception as e:
        print(e)
        conexao.rollback()
        return False


def delete_cidade(id):
    conexao = conectar_pymysql()
    cursor = conexao.cursor()

    try:
        sql = "DELETE FROM cidades WHERE id_c=%s"
        cursor.execute(sql,(id,))
        conexao.commit()
        return True
    except Exception as e:
        print(e)
        conexao.rollback()
        return False
    

def select_pesquisa(str):
    conexao   = conectar_pymysql()
    cursor    = conexao.cursor()
 
    pesquisa  = "%"+str+"%"
    sql       = "SELECT * FROM cidades WHERE nome_c LIKE %s OR pais_c LIKE %s OR desc_c LIKE %s ORDER BY nome_c ASC";
    cursor.execute(sql,(pesquisa,pesquisa,pesquisa))
    resultado = cursor.fetchall()

    return(resultado)

    
if __name__ == "__main__":
    pprint(select_imagens_cidade(1))