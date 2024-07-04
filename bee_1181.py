def calcular_media(valores: list) -> float:
    return sum(valores)/len(valores)


linha = int(input())
operacao = input()
matriz = [[] for _ in range(12)]

for i in range(12):
    for j in range(12):
        matriz[i].append(float(input()))

if operacao == 'S':
    soma = sum(matriz[linha])
    print(f"{soma:.1f}")
else:
    media = calcular_media(matriz[linha])
    print(f"{media:.1f}")
