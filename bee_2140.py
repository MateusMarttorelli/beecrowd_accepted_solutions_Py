notas_disponiveis = [100, 50, 20, 10, 5, 2]

while True:
    valor_compra, valor_pago = map(int, input().split())

    if valor_compra == valor_pago == 0:
        break

    troco = valor_pago - valor_compra
    num_notas_para_troco = 2

    for nota in notas_disponiveis:
        if troco - nota >= 0:
            troco -= nota
            num_notas_para_troco -= 1

        if num_notas_para_troco == 0 or troco == 0:
            break

    if troco == 0 and num_notas_para_troco == 0:
        print("possible")
    else:
        print("impossible")