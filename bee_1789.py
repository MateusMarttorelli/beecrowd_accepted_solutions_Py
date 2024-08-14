while True:

    try:
        n_lesmas = int(input())
        lista_de_lesmas = list(map(int, input().split()))

        if max(lista_de_lesmas) < 10:
            print(1)
        elif max(lista_de_lesmas) < 20:
            print(2)
        else:
            print(3)

    except EOFError:
        break
