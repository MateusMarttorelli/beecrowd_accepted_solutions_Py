import math

while True:

    valores = input().strip()

    if valores == '0':
        break

    x, y, percentual = map(int, valores.split())

    terreno_necessario = (x * y) * (100 / percentual)
    tamanho_dos_lados = math.sqrt(terreno_necessario)

    print(int(tamanho_dos_lados))
