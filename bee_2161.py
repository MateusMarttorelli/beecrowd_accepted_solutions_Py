n = int(input())

resultado = 0

for _ in range(n):
    resultado = 1 / (6 + resultado)

resultado += 3

print(f"{resultado:.10f}")