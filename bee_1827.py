while True:
    try:
        n = int(input())
        matriz = [[0 for _ in range(n)] for _ in range(n)]
        margem = n // 3
        intervalo_quadrado_interno = range(margem, n - margem)

        for i in range(n):
            for j in range(n):
                if i == j and i == n // 2:
                    matriz[i][j] = 4
                elif i in intervalo_quadrado_interno and j in intervalo_quadrado_interno:
                    matriz[i][j] = 1
                elif i == j:
                    matriz[i][j] = 2
                elif i + j == n - 1:
                    matriz[i][j] = 3

        for linha in matriz:
            print(''.join(map(str, linha)))

        print("")

    except EOFError:
        break