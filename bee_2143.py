while True:
    casos_de_teste = int(input())

    if casos_de_teste == 0:
        break

    for _ in range(casos_de_teste):
        n_pessoas_mesa = int(input())

        if n_pessoas_mesa % 2 == 0:
            n_pedidos = (n_pessoas_mesa * 2) - 2
        else:
            n_pedidos = (n_pessoas_mesa * 2) - 1

        print(n_pedidos)
