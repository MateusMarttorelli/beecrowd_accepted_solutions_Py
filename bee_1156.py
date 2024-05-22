soma = 0
i = 1.0
j = 1.0

while i < 39:
    soma = soma + i/j
    i += 2
    j *= 2

print(f"{soma:.2f}")
