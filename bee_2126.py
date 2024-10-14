caso = 1

try:
    while True:
        sequencia_1 = input()
        sequencia_2 = input()

        qtd_subsequencias = sequencia_2.count(sequencia_1)

        if qtd_subsequencias == 0:
            print(f"Caso #{caso}:\nNao existe subsequencia\n")

        else:
            posicao_subsequencia = sequencia_2.rfind(sequencia_1) + 1
            print(f"Caso #{caso}:\nQtd.Subsequencias: {qtd_subsequencias}\nPos: {posicao_subsequencia}\n")

        caso += 1

except EOFError:
    pass
