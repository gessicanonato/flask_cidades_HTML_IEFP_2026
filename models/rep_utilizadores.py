from app.db_config import conectar_pymysql
from pprint import pprint


def select_todos_utilizadores():
    """Lista todos os utilizadores

    Returns:
        _type_: _description_
    """    
    conexao     = conectar_pymysql()
    cursor      = conexao.cursor()
    query       = "SELECT * FROM utilizadores"
    
    try:
        cursor.execute(query)
        resultado   = cursor.fetchall()
    except Exception as e:
        print(e)
        return []
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()    

    return resultado



def select_nome_do_utilizador(utilizador_id):
    """Devolve o nome de um utilizador

    Returns:
        string: o nome do utilizador
    """    
    conexao     = conectar_pymysql()
    cursor      = conexao.cursor()
    query       = "SELECT nome_u FROM utilizadores WHERE id_u = %s"

    try:
        cursor.execute(query,(utilizador_id,))
        resultado = cursor.fetchone()
    except Exception as e:
        print(e)
        return "Utilizador não encontrado"
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
   
    return resultado['nome_u']     # type:ignore



def insert_utilizador(nome, password, nivel):
    conexao = conectar_pymysql()
    cursor  = conexao.cursor()

    try:
        query = "INSERT INTO utilizadores (nome_u, ppass_u, nivel_u) VALUES (%s,%s,%s)"
        cursor.execute(query,(nome, password, nivel))
        conexao.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
    
    


if __name__ == "__main__":
    pprint(select_todos_utilizadores())