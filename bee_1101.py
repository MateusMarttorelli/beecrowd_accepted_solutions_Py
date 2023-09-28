while True:
    m, n = map(int, input().split())

    if m <= 0 or n <= 0:
        break

    if m > n:
        m, n = n, m

    soma = 0

    for num in range(m, n + 1):
        print(num, end=' ')
        soma += num

    print(f"Sum={soma}")
