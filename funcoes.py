import random

def rolar_dados(vezes):
    dados = [] #cria a lista dos dados
    for i in range(vezes): #repete o ciclo uma quantidade especifica
        dado = random.randint(1,6) #pega um numero entre 1 e 6
        dados.append(dado) #adiciona o numero na lista dos dados
    return dados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_no_estoque.append(dados_rolados[dado_para_guardar]) #adiciona o dado selecionado no estoque 
    dados_rolados.pop(dado_para_guardar) #remove o dado selecionado dos dados rolados
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_retirar):
    dados_rolados.append(dados_no_estoque[dado_para_retirar])
    dados_no_estoque.pop(dado_para_retirar)
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados_rolados):
    pontuacao = {} #cria o dicionario
    for dado in dados_rolados:
        chave = dado #chave do dic = ao valor do dado
        pontuacao[chave] = pontuacao.get(chave, 0) + dado #adiciona o valor do dado para o dicionario, se nao existir = 0
    for i in range(1,7):
        pontuacao[i] = pontuacao.get(i, 0) # coloca os numeros que nao sairam nos dados
    return dict(sorted(pontuacao.items()))

def calcula_pontos_soma (dados_rolados):
    n = 0
    r = 0
    while len(dados_rolados) > n :
        x = dados_rolados[n]
        r = r + x
        n += 1
    return(r)

def calcula_pontos_sequencia_baixa (dados_rolados):
    dados_rolados = sorted(dados_rolados)
    n = 0
    r = 0
    y = 0
    m = 0
    while len(dados_rolados)-1 > n :
        if dados_rolados[n+1] == dados_rolados[n]:
            y = 0
        elif dados_rolados[n+1] - dados_rolados[n] == 1:
            y = 1
        m = m + y
        n += 1
    if m >= 4:
        r = 15
    return(r)

