from app.models.rep_cidades import select_todas_cidades, select_cidade, select_imagens_cidade, insert_into_cidade, update_cidade, delete_cidade, select_pesquisa
from pprint import pprint


def lista_cidades():
    return select_todas_cidades()


def detalhes_cidade(cidade_id):
    dados = select_cidade(cidade_id)
    if int(dados['dataf_c']) < 0:
        ano = str(abs(dados['dataf_c'])) + " AC"
        dados['dataf_AC'] = ano

    fotos = select_imagens_cidade(cidade_id)
    dados_finais = [dados, fotos]

    return dados_finais


def adicionar_cidade(nome, dataf, pais, habitantes, desc):
    return insert_into_cidade(nome, dataf, pais, habitantes, desc)


def atualizar_cidade(id, nome, dataf, pais, habitantes, desc):
    return update_cidade(id, nome, dataf, pais, habitantes, desc)


def eliminar_cidade(id):
    return delete_cidade(id)


def pesquisa_cidades(str):
    dados = select_pesquisa(str)
    lista_final = []
    for cidade in dados:
        dadosPesquisados = {
            "id"    : cidade['id_c'],
            "nome"  : cidade['nome_c'],
            "desc"  : desc_resumo_pesq(cidade['desc_c'],str)    
        }
        lista_final.append(dadosPesquisados)
    return (str,lista_final)


def desc_resumo_pesq(desc, pesq):
    desc_l = desc.lower()
    pesq_l = pesq.lower()

    tamanho = len(desc)
    tamanho_pesq = len(pesq)

    posicao = desc_l.find(pesq_l)

    # Se não encontrou a pesquisa
    if posicao == -1:
        return desc[:220] + ("..." if len(desc) > 220 else "")

    str_sem_negrito = desc[posicao:posicao + tamanho_pesq]

    qtos_car = 110
    inicio = 0 if posicao < qtos_car else posicao - qtos_car

    reticencias_inicio = "..." if posicao > qtos_car else ""
    reticencias_final = "..." if posicao < (tamanho - qtos_car) else ""

    resumo = desc[inicio:inicio + qtos_car * 2]
    resposta = reticencias_inicio + resumo + reticencias_final

    # Substituição ignorando maiúsculas/minúsculas
    import re
    substituto = f"<strong>{str_sem_negrito}</strong>"
    resposta = re.sub(
        re.escape(pesq),
        substituto,
        resposta,
        flags=re.IGNORECASE
    )

    return resposta


if __name__ == "__main__":
    pprint("batatas")