renda = float(input())

if renda <= 2000:
    imposto = 0
elif renda <= 3000:
    imposto = 0.08 * (renda - 2000)
elif renda <= 4500:
    imposto = 80 + (0.18 * (renda - 3000))
else:
    imposto = 80 + 270 + (0.28 * (renda - 4500))

if imposto == 0:
    print('Isento')
else:
    print(f'R$ {imposto:.2f}')
