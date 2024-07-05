coluna = int(input())
operacao = input()
matriz = [[] for _ in range(12)]

for i in range(12):
    for j in range(12):
        matriz[i].append(float(input()))

if operacao == 'S':
    soma = 0
    for i in range(12):
        soma += matriz[i][coluna]

    print(f"{soma:.1f}")

else:
    soma = 0
    for i in range(12):
        soma += matriz[i][coluna]

    media = soma / 12
    print(f"{media:.1f}")