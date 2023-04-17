num_positivos = 0

for i in range(6):
    if float(input()) > 0:
        num_positivos += 1

print(f'{num_positivos} valores positivos')
