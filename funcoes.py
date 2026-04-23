import random

def rolar_dados(vezes):
    dados = []
    for i in range(vezes):
        dado = random.randint(1,6)
        dados.append(dado)
    return dados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_no_estoque.append(dados_rolados(dado_para_guardar))
    dados_rolados.pop(dado_para_guardar)
    return [dados_rolados, dados_no_estoque]