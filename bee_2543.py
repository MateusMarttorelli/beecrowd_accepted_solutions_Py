while True:
    try:
        gameplays_cs = 0

        n_gameplays, id_pessoal = map(int, input().split())

        for _ in range(n_gameplays):
            id_jogador, jogo = map(int, input().split())

            if id_jogador == id_pessoal and jogo == 0:
                gameplays_cs += 1

        print(gameplays_cs)

    except EOFError:
        break