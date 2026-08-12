n = int(input())

for _ in range(n):
    x = int(input())
    binario = bin(x)[2:]

    print(len(max(binario.split("0"), key=len)))


