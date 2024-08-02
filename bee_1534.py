import sys

entrada = sys.stdin.read
dados = entrada().strip().split()

for value in dados:
    n = int(value)

    if n < 3 or n >= 70:
        continue

    for i in range(n):
        linha = []

        for j in range(n):
            if i + j == n - 1:
                valor = 2
            elif i == j:
                valor = 1
            else:
                valor = 3
            linha.append(str(valor))

        print(''.join(linha))
