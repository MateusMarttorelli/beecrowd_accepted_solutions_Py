def encontrar_posicao(matriz, valor):
    for x, linha in enumerate(matriz):
        for y, elemento in enumerate(linha):
            if elemento == valor:
                return x, y
    return None

while True:
    try:
        n, m = map(int, input().split())
        matriz = []

        for _ in range(n):
            linha = list(map(int, input().split()))
            matriz.append(linha)

        posicao1 = encontrar_posicao(matriz, 1)
        posicao2 = encontrar_posicao(matriz, 2)

        distancia = abs(posicao1[0] - posicao2[0]) + abs(posicao1[1] - posicao2[1])
        print(distancia)

    except EOFError:
        break

