n = int(input())

for i in range(n):
    x = int(input())
    soma_divisores = 0

    for j in range(1, x//2 + 1):
        if x % j == 0:
            soma_divisores += j

    if soma_divisores == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
