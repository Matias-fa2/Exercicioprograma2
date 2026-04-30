from funcoes import *
pontuacao = 0
rodada = 0
rerrolou = 0
dados_rolados = []
dados_guardados = []
ja_foi = []
cartela = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1,
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
dados_rolados = rolar_dados(5) 
imprime_cartela(cartela)
while rodada < 12:
    print(f'Dados rolados: {dados_rolados}')
    print(f'Dados guardados: {dados_guardados}')
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    opcao = input()

    while opcao not in ['0', '1', '2', '3', '4']:
        print("Opção inválida. Tente novamente.")
        opcao = input()

    opcao = int(opcao)
    if opcao == 1:
        print("Digite o índice do dado a ser guardado (0 a 4):")
        indice = int(input())
        if 0 <= indice < len(dados_rolados):
            guardar_dado(dados_rolados, dados_guardados, indice)
    elif opcao == 2:
        if len(dados_guardados) > 0:
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            if 0 <= indice < len(dados_guardados):
                remover_dado(dados_rolados, dados_guardados, indice)
    elif opcao == 3:
        if rerrolou < 2:
            rerrolou += 1
            dados_rolados = rolar_dados(len(dados_rolados))
        else:
            print("Você já usou todas as rerrolagens.")
    elif opcao == 0:
        print("Digite a combinação desejada:")
        combinacao = input()
        if combinacao.isdigit():
            combinacao = int(combinacao)
        while True:
            if combinacao not in cartela['regra_avancada'] and combinacao not in cartela['regra_simples']:
                print("Combinação inválida. Tente novamente.")
            elif combinacao in ja_foi:
                print("Essa combinação já foi utilizada.")
            else:
                break
            combinacao = input()
            if combinacao.isdigit():
                combinacao = int(combinacao)
        faz_jogada(dados_rolados + dados_guardados, combinacao, cartela)
        ja_foi.append(combinacao)
        dados_rolados = rolar_dados(5)
        dados_guardados = []
        rerrolou = 0
        rodada += 1
    elif opcao == 4:
        imprime_cartela(cartela)

    


imprime_cartela(cartela)

pontuacao_simples = sum(cartela['regra_simples'].values())
for combinacao in cartela['regra_avancada']:
    pontuacao += cartela['regra_avancada'][combinacao]
pontuacao += pontuacao_simples

if pontuacao_simples >= 63:
    pontuacao += 35

print(f"Pontuação total: {pontuacao}")