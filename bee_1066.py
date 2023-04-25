num_pares = 0
num_impares = 0
num_positivos = 0
num_negativos = 0

for i in range(5):
    num = float(input())
    if num > 0:
        num_positivos += 1
    elif num < 0:
        num_negativos += 1

    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1

print(f'{num_pares} valor(es) par(es)')
print(f'{num_impares} valor(es) impar(es)')
print(f'{num_positivos} valor(es) positivo(s)')
print(f'{num_negativos} valor(es) negativo(s)')
