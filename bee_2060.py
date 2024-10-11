qtd_numeros = int(input())
numeros = list(map(int, input().split()))

mult2 = 0
mult3 = 0
mult4 = 0
mult5 = 0

for n in numeros:
    if n % 2 == 0:
        mult2 += 1
    if n % 3 == 0:
        mult3 += 1
    if n % 4 == 0:
        mult4 += 1
    if n % 5 == 0:
        mult5 += 1

print(f'''{mult2} Multiplo(s) de 2
{mult3} Multiplo(s) de 3
{mult4} Multiplo(s) de 4
{mult5} Multiplo(s) de 5''')