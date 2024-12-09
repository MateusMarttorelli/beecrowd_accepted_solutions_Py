n_linhas, n_colunas = map(int, input().split())

matriz = list()

for i in range(n_linhas):
    matriz.append(list(map(int, input().split())))

encontrado = False
x, y = 0, 0

for i in range(n_linhas - 2):
    for j in range(1, n_colunas - 1):
        if (
            matriz[i][j] == 7 and
            matriz[i + 1][j - 1] == 7 and
            matriz[i + 1][j] == 42 and
            matriz[i + 1][j + 1] == 7 and
            matriz[i + 2][j] == 7
        ):
            x, y = i + 2, j + 1
            encontrado = True
            break

    if encontrado:
        break

print(x, y)

