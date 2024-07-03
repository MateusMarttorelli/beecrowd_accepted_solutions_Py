n = int(input())

x = list(map(int, input().split()))

menor_valor = min(x)

print(f"Menor valor: {menor_valor}")
print(f"Posicao: {x.index(menor_valor)}")
