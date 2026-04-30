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

def calcula_pontos_sequencia_baixa(dados_rolados):
    dados_rolados = sorted(set(dados_rolados))  
    s = 1 
    i = 0
    while i < len(dados_rolados) - 1:
        if dados_rolados[i+1] - dados_rolados[i] == 1:
            s += 1
            if s >= 4:
                return 15
        else:
            s = 1
        i+=1
    return 0

def calcula_pontos_sequencia_alta(dados_rolados):
    dados_rolados = sorted(set(dados_rolados))  
    s = 1 
    i = 0
    while i < len(dados_rolados) - 1:
        if dados_rolados[i+1] - dados_rolados[i] == 1:
            s += 1
            if s >= 5:
                return 30
        else:
            s = 1
        i+=1

    return 0

def calcula_pontos_full_house (dados_rolados):
    contagens = {}
    i = 0
    n = 0
    s = 0
    while i < len(dados_rolados):
        valor = dados_rolados[i]
        if valor in contagens:
            contagens[valor] += 1
        else:
            contagens[valor] = 1
        i += 1
    valores = list(contagens.values())
    if sorted(valores) == [2, 3]:
        while n < len(dados_rolados):
            s = s + dados_rolados[n]
            n += 1
        return (s)
    return 0

def calcula_pontos_quadra (dados_rolados):
    dados_rolados = sorted(dados_rolados)
    i = 0
    s = 0
    n = 0
    while i < len(dados_rolados):
        e = 0
        x = 0
        while e < len(dados_rolados):
            if dados_rolados[i] == dados_rolados[e]:
                x += 1
            if x >= 4:
                while n < len(dados_rolados):
                    s = s + dados_rolados[n]
                    n += 1
                return(s)
            e += 1
        i += 1
    return 0

def calcula_pontos_quina (dados_rolados):
    dados_rolados = sorted(dados_rolados)
    i = 0
    while i < len(dados_rolados):
        e = 0
        x = 0
        while e < len(dados_rolados):
            if dados_rolados[i] == dados_rolados[e]:
                x += 1
            if x >= 5:
                return 50
            e += 1
        i += 1
    return 0

def calcula_pontos_regra_avancada(dados_rolados):
    dict_dados = {}
    dict_dados['cinco_iguais'] = calcula_pontos_quina(dados_rolados)
    dict_dados['full_house'] = calcula_pontos_full_house(dados_rolados)
    dict_dados['quadra'] = calcula_pontos_quadra(dados_rolados)
    dict_dados['sem_combinacao'] = calcula_pontos_soma(dados_rolados)
    dict_dados['sequencia_alta'] = calcula_pontos_sequencia_alta(dados_rolados)
    dict_dados['sequencia_baixa'] = calcula_pontos_sequencia_baixa(dados_rolados)
    return dict_dados


def faz_jogada(dados, categoria, dict_cartela):
    jogadas_avancada = ['cinco_iguais', 'full_house', 'quadra', 'sem_combinacao', 'sequencia_alta', 'sequencia_baixa']
    jogadas_simples = '123456'
    if categoria in jogadas_avancada:
        dict_cartela['regra_avancada'][categoria] = calcula_pontos_regra_avancada(dados)[categoria]
    elif categoria in jogadas_simples:
        dict_cartela['regra_simples'][int(categoria)] = calcula_pontos_regra_simples(dados)[int(categoria)]
    
    return dict_cartela