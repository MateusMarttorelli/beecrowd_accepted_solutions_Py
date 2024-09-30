caso = 0

while True:

    caso += 1

    try:
        n = int(input())
        sequencia = [0]

        for i in range(n + 1):
            sequencia += [i] * i

        qtd_numeros = len(sequencia)

        print(f"Caso {caso}: {qtd_numeros} {"numero" if qtd_numeros == 1 else "numeros"}")
        print(" ".join(map(str, sequencia)))

    except EOFError:
        break