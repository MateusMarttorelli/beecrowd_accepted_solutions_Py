numero_de_casos = int(input())

for _ in range(numero_de_casos):
    anos_transcorridos = int(input())
    ano = 2015 - anos_transcorridos

    if ano <= 0:
        print(f"{abs(ano-1)} A.C.")
    else:
        print(f"{ano} D.C.")