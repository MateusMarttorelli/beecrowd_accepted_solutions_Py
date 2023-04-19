num_positivos = 0
media = 0

for i in range(6):
    num = float(input())
    if num > 0:
        num_positivos += 1
        media += num

print(f'{num_positivos} valores positivos')
print(f'{media/num_positivos:.1f}')
