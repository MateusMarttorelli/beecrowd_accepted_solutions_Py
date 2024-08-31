casos_de_teste = int(input())

for _ in range(casos_de_teste):

    jogador1, escolha1, jogador2, escolha2 = input().split()
    numero_jogador1, numero_jogador2 = map(int, input().split())

    if (numero_jogador1 + numero_jogador2) % 2 == 0:
        if escolha1 == "PAR":
            print(jogador1)
        else:
            print(jogador2)
    else:
        if escolha1 == "IMPAR":
            print(jogador1)
        else:
            print(jogador2)
