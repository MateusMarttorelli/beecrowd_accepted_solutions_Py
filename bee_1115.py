while True:
    coordenada = list(map(int, input().split()))

    if coordenada[0] > 0 and coordenada[1] > 0:
        print("primeiro")
    elif coordenada[0] < 0 and coordenada[1] > 0:
        print("segundo")
    elif coordenada[0] < 0 and coordenada[1] < 0:
        print("terceiro")
    elif coordenada[0] > 0 and coordenada[1] < 0:
        print("quarto")
    else:
        break
