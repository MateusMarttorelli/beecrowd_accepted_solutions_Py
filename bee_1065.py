num_pares = 0

for i in range(5):
    if int(input()) % 2 == 0:
        num_pares += 1

print(f'{num_pares} valores pares')
