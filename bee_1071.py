x = int(input())
y = int(input())

if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = x

soma = 0

for num in range(menor + 1, maior):
    if num % 2 != 0:
        soma += num

print(soma)
