while True:
    n = int(input())

    if n == 0:
        break

    maior_valor = 2**(2*n - 2)
    digito = len(str(maior_valor))

    matriz = [[2**(i+j) for j in range(n)] for i in range(n)]

    for linha in matriz:
        print(' '.join(f"{num:{digito}}" for num in linha))

    print()

