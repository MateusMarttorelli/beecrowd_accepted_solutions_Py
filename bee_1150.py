x = int(input())

while True:
    z = int(input())
    if z > x:
        break

soma = x
contagem = 1

while soma <= z:
    x += 1
    soma += x
    contagem += 1

print(contagem)
