operacao = input()
matriz = [[] for _ in range(12)]

for i in range(12):
    for j in range(12):
        matriz[i].append(float(input()))

soma = 0
contador = 0

for i in range(12):
    for j in range(0, 11 - i):
        soma += matriz[i][j]
        contador += 1

if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    media = soma / contador
    print(f"{media:.1f}")
