lanches = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

pedido, quantidade = list(map(int, input().split()))
total = lanches[pedido] * quantidade

print(f'Total: R$ {total:.2f}')
