while True:
    try:
        n, d = map(int, input().split())
        melhor_dia = None

        for _ in range(d):
            linha = input().split()
            dia = linha[0]
            disponibilidade = map(int, linha[1:])

            if all(disponibilidade) and melhor_dia == None:
                melhor_dia = dia

        if melhor_dia is None:
            print("Pizza antes de FdI")
        else:
            print(melhor_dia)

    except EOFError:
        break




