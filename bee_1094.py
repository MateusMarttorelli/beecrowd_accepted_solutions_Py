n = int(input())
cobaias = 0
coelhos = 0
ratos = 0
sapos = 0

for i in range(n):
    qtd, tipo = input().split()

    if tipo == 'C':
        coelhos += int(qtd)
    elif tipo == 'R':
        ratos += int(qtd)
    else:
        sapos += int(qtd)

    cobaias += int(qtd)

percentual_coelhos = (coelhos/cobaias) * 100
percentual_ratos = (ratos/cobaias) * 100
percentual_sapos = (sapos/cobaias) * 100

print(f"Total: {cobaias} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print("Percentual de coelhos: {:.2f} %".format(percentual_coelhos))
print("Percentual de ratos: {:.2f} %".format(percentual_ratos))
print("Percentual de sapos: {:.2f} %".format(percentual_sapos))
