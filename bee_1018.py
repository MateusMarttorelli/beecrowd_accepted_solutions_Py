notas = {'nota100': 100, 'nota50': 50, 'nota20': 20, 'nota10': 10, 'nota5': 5, 'nota2': 2, 'nota1': 1}

valor = int(input())

print(f'{valor}')

for i, j in notas.items():
    notas[i] = valor//j
    valor -= notas[i]*j

    print(f'{notas[i]} nota(s) de R$ {j:.2f}'.replace('.', ','))
