while True:
    while True:
        nota1 = float(input())

        if nota1 < 0 or nota1 > 10:
            print("nota invalida")
            continue
        else:
            break

    while True:
        nota2 = float(input())

        if nota2 < 0 or nota2 > 10:
            print("nota invalida")
            continue
        else:
            break

    media = (nota1 + nota2) / 2
    print(f"media = {media:.2f}")

    while True:
        print(f"novo calculo (1-sim 2-nao)")
        resposta = int(input())

        if resposta == 1:
            break
        elif resposta == 2:
            exit(0)
        else:
            continue
