par_ou_impar, j1, j2, roubou, acusou = map(int, input().split())

if roubou == 1 and acusou == 1:
    print("Jogador 2 ganha!")
elif roubou == 1 and acusou == 0:
    print("Jogador 1 ganha!")
elif roubou == 0 and acusou == 1:
    print("Jogador 1 ganha!")
else:
    soma = j1 + j2

    if soma % 2 == 0 and par_ou_impar == 1:
        print("Jogador 1 ganha!")
    elif soma % 2 != 0 and par_ou_impar == 0:
        print("Jogador 1 ganha!")
    else:
        print("Jogador 2 ganha!")
