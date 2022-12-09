produto01 = input().split()
produto02 = input().split()

cod01, qtd01, preco01 = produto01
cod02, qtd02, preco02 = produto02

valor_total = int(qtd01)*float(preco01) + int(qtd02)*float(preco02)

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')
