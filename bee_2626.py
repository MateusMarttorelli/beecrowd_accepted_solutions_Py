while True:
    try:
        condicoes_vitoria = {
            "pedra": ("tesoura", "tesoura"),
            "papel": ("pedra", "pedra"),
            "tesoura": ("papel", "papel")
        }

        dodo, leo, pepper = input().split()

        if condicoes_vitoria[dodo] == (leo, pepper):
            print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
        elif condicoes_vitoria[leo] == (dodo, pepper):
            print("Iron Maiden's gonna get you, no matter how far!")
        elif condicoes_vitoria[pepper] == (dodo, leo):
            print("Urano perdeu algo muito precioso...")
        else:
            print("Putz vei, o Leo ta demorando muito pra jogar...")

    except EOFError:
        break