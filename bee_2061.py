n_abas, n_acoes = map(int, input().split())

for _ in range(n_acoes):
    acao = input()

    if acao == "fechou":
        n_abas += 1
    elif acao == "clicou":
        n_abas -= 1

print(n_abas)
