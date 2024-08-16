regras = {
    "tesoura": ["papel", "lagarto"],
    "papel": ["pedra", "Spock"],
    "pedra": ["lagarto", "tesoura"],
    "lagarto": ["Spock", "papel"],
    "Spock": ["tesoura", "pedra"]
}

t = int(input())

for i in range(1, t + 1):
    sheldon, raj = input().split()

    if sheldon == raj:
        resultado = "De novo!"
    elif raj in regras[sheldon]:
        resultado = "Bazinga!"
    else:
        resultado = "Raj trapaceou!"

    print(f"Caso #{i}: {resultado}")
