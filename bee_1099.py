n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    soma_impar = 0

    if x > y:
        x, y = y, x

    for j in range(x+1, y):
        if j % 2 != 0:
            soma_impar += j

    print(soma_impar)
