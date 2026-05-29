while True:
    try:
        n = int(input())

        expressoes = [input() for _ in range(n)]
        reprovados = []

        for _ in range(n):
            nome, idx, operador = input().split()
            x, y, z = map(int, expressoes[int(idx) - 1].replace("=", " ").split())

            correta = (
                (operador == "+" and x + y == z) or
                (operador == "-" and x - y == z) or
                (operador == "*" and x * y == z) or
                (operador == "I" and x + y != z and x - y != z and x * y != z)
            )

            if not correta:
                reprovados.append(nome)

        if not reprovados:
            print("You Shall All Pass!")
        elif len(reprovados) == n:
            print("None Shall Pass!")
        else:
            print(" ".join(sorted(reprovados)))

    except EOFError:
        break