while True:
    n = int(input())

    if n == 0:
        break

    for i in range(n):
        linha = []

        for j in range(n):
            linha.append(f"{min(i+1, j+1, n - i, n - j):3}")

        print('   '.join(linha))

    print()
