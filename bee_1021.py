notas = {'nota100': 100, 'nota50': 50, 'nota20': 20, 'nota10': 10, 'nota5': 5, 'nota2': 2}
moedas = {'moeda100': 1, 'moeda50': 0.50, 'moeda25': 0.25, 'moeda10': 0.10, 'moeda5': 0.05, 'moeda1': 0.01}

valor = float(input())

print(f'NOTAS:')
for i, j in notas.items():
    notas[i] = int(valor/j)
    valor = round(valor - (notas[i]*j), 2)

    print(f'{notas[i]} nota(s) de R$ {j:.2f}')

print(f'MOEDAS:')
for i, j in moedas.items():
    moedas[i] = int(valor/j)
    valor = round(valor - (moedas[i]*j), 2)

    print(f'{moedas[i]} moeda(s) de R$ {j:.2f}')
