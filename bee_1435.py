while True:
    n = int(input())

    if n == 0:
        break

    for i in range(n):
        linha = []

        for j in range(n):
            linha.append(str(min(i+1, j+1, n - i, n - j)))

        print('   '.join(linha))

    print()
