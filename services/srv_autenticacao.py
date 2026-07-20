from app.models.rep_autenticacao import validar_dados_de_login
from werkzeug.security import check_password_hash


def validar_login(utilizador, password):
    """
    Valida credenciais de login sem efeitos colaterais (stateless).

    Args:
        nome do utilizador.
        password (str): Password em texto simples.

    Returns:
        dict:
            {
                "sucesso": bool,
                "mensagem": str (opcional),
                "utilizador": dict (opcional)
            }
    """

    dados = validar_dados_de_login(utilizador)

    if "mensagem" in dados:
        return {
            "sucesso": False,
            "mensagem": dados["mensagem"]
        }

    if check_password_hash(dados["ppass_u"], password):
        return {
            "sucesso": True,
            "utilizador": {
                "id": dados["id_u"],
                "nome": dados["nome_u"],
                "nivel": dados["nivel_u"]
            }
        }

    return {
        "sucesso": False,
        "mensagem": "Password incorreta"
    }
        