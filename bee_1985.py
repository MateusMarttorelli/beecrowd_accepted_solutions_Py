n_produtos_comprados = int(input())

produtos = {1001: 1.5, 1002: 2.5, 1003: 3.5, 1004: 4.5, 1005: 5.5}
total = 0

for _ in range(n_produtos_comprados):
    codigo, quantidade = map(int, input().split())
    total += quantidade * produtos[codigo]

print(f"{total:.2f}")