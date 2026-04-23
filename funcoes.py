import random

def rolar_dados(vezes):
    dados = []
    for i in range(vezes):
        dado = random.randint(1,6)
        dados.append(dado)
    return dados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    dados_rolados.pop(dado_para_guardar)
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_retirar):
    dados_rolados.append(dados_no_estoque[dado_para_retirar])
    dados_no_estoque.pop(dado_para_retirar)
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados_rolados):
    pontuacao = {}
    for dado in dados_rolados:
        chave = str(dado)
        pontuacao[chave] = pontuacao.get(chave, 0) + dado
    for i in range(1,7):
        pontuacao[str(i)] = pontuacao.get(str(i), 0)
    return dict(sorted(pontuacao.items()))
dados = [1,2,5,5,6]
print(calcula_pontos_regra_simples(dados))