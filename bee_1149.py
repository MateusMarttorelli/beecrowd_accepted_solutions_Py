entrada = list(map(int, input().split()))

a = entrada[0]
n = 0
soma = 0

for i in entrada[1:]:
    if i > 0:
        n = i

for i in range(0, n):
    soma = soma + a + i

print(soma)
