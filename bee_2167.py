n = int(input())
r = list(map(int, input().split()))

rotacao_anterior = 0
indice_menor_rotacao = 0

for i, rotacao in enumerate(r):
    if rotacao < rotacao_anterior:
        indice_menor_rotacao = i + 1
        break
    else:
        rotacao_anterior = rotacao

print(indice_menor_rotacao)