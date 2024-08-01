while True:
    n = int(input(''))

    if n == 0:
        break

    for i in range(n):
        linha = []

        for j in range(n):
            linha.append(f"{max(i - j + 1, j - i + 1):3}")

        print(' '.join(linha))

    print()
