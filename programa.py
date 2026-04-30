from funcoes import *
pontuacao = 0
rodada = 0
rerrolou = 0
dados_rolados = []
dados_guardados = []
ja_foi = []
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
dados_rolados = rolar_dados(5) 
imprime_cartela(cartela)
while rodada < 12:
    print(f'Dados rolados: {dados_rolados}')
    print(f'Dados guardados: {dados_guardados}')
    opcao = input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    while opcao not in '01234' or opcao == '':
        print("Opção inválida. Tente novamente.")
        opcao = input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    opcao = int(opcao)
    if opcao == 1:
        indice = int(input("Digite o índice do dado a ser guardado (0 a 4):"))
        guardar_dado(dados_rolados, dados_guardados, indice)
    elif opcao == 2:
        if len(dados_guardados) > 0:
            indice = int(input("Digite o índice do dado a ser removido (0 a 4):"))
            remover_dado(dados_rolados, dados_guardados, indice)

    elif opcao == 3:
        rerrolou +=1
        if rerrolou < 3:
            dados_rolados = rolar_dados(len(dados_rolados))
        else:
            print("Você já usou todas as rerrolagens.")  
    elif opcao == 0:
        combinacao = input("Digite a combinação desejada:")
        if combinacao.isdigit(): combinacao = int(combinacao)
        while combinacao not in cartela['regra_avancada'] and combinacao not in cartela['regra_simples']:
            print("Combinação inválida. Tente novamente.")
            combinacao = input("Digite a combinação desejada:")
            if combinacao.isdigit(): combinacao = int(combinacao)
        
        if combinacao not in ja_foi:
            faz_jogada(dados_rolados, combinacao, cartela)
            ja_foi.append(combinacao)
            dados_rolados = rolar_dados(5)
            dados_guardados = []
            rerrolou = 0
            rodada+=1
            
    elif opcao == 4:
        imprime_cartela(cartela)

    


for tipo in cartela:
    for combinacao in cartela[tipo]:
        pontuacao += cartela[tipo][combinacao]

print(f"Pontuação total: {pontuacao}")