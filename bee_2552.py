while True:
    try:
        n, m = map(int, input().split())

        matriz_entrada = [list(map(int, input().split())) for _ in range(n)]
        matriz_saida = [[0] * m for _ in range(n)]

        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita

        for i in range(n):
            for j in range(m):

                if matriz_entrada[i][j] == 1:
                    matriz_saida[i][j] = 9
                    continue

                pontuacao = 0
                for di, dj in direcoes:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and matriz_entrada[ni][nj] == 1:
                        pontuacao += 1

                matriz_saida[i][j] = pontuacao

        for linha in matriz_saida:
            print(*linha, sep='')

    except EOFError:
        break
