from app.db_config import conectar_pymysql


def validar_dados_de_login(nome_de_utilizador):
    """
    Obtém os dados de um utilizador a partir do nome de utilizador.
    Returns:
        dict:{"id_u": int, "nome_u": str, "ppass_u": str}
        ou {"mensagem": str}
    """

    conexao = conectar_pymysql()
    cursor = conexao.cursor()

    query = """
        SELECT id_u, nome_u, ppass_u, nivel_u
        FROM utilizadores
        WHERE nome_u = %s
    """

    try:
        cursor.execute(query, (nome_de_utilizador,))
        resultado = cursor.fetchone()

        if not resultado:
            return {"mensagem": "O utilizador não foi encontrado"}

        return {
            "id_u": resultado["id_u"],
            "nome_u": resultado["nome_u"],
            "ppass_u": resultado["ppass_u"],
            "nivel_u": resultado["nivel_u"]
        }
    except Exception as e:
        return {
            "mensagem": "Erro na base de dados.",
            "erro": str(e)
        }
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

