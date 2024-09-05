reguas_de_tomadas = list(map(int, input().split()))

n_maximo_aparelhos = sum(reguas_de_tomadas) - 3

print(n_maximo_aparelhos)
