from funcoes import *

rodada = 0
dados_rolados = []
dados_guardados = []

cartela = {
    'regra_simples': {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    },
    'regra_avancada': {
        'sem_combinacao': 0,
        'quadra': 0,
        'full_house': 0,
        'sequencia_baixa': 0,
        'sequencia_alta': 0,
        'cinco_iguais': 0
    }
}

imprime_cartela(cartela)
while rodada < 12:
    if rodada == 0:
        dados_rolados = rolar_dados(5)
    else:
        dados_rolados = rolar_dados(len(dados_rolados))
    
    print()
    rodada+=1