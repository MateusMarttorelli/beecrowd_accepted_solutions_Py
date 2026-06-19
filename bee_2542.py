while True:
    try:
        n = int(input())
        n_cartas_marcos, n_cartas_leonardo = map(int, input().split())

        cartas_marcos = [list(map(int, input().split())) for _ in range(n_cartas_marcos)]
        cartas_leonardo = [list(map(int, input().split())) for _ in range(n_cartas_leonardo)]

        carta_escolhida_marcos, carta_escolhida_leonardo = map(int, input().split())
        atributo_sorteado = int(input())

        valor_marcos = cartas_marcos[carta_escolhida_marcos - 1][atributo_sorteado - 1]
        valor_leonardo = cartas_leonardo[carta_escolhida_leonardo - 1][atributo_sorteado - 1]

        if valor_marcos > valor_leonardo:
            print("Marcos")
        elif valor_marcos < valor_leonardo:
            print("Leonardo")
        else:
            print("Empate")

    except EOFError:
        break
