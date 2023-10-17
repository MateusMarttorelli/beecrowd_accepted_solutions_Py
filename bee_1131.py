grenais = 0
vitorias_gremio = 0
vitorias_inter = 0
empates = 0

while True:

    placar_grenal = list(map(int, input().split()))

    if placar_grenal[0] > placar_grenal[1]:
        vitorias_inter += 1
    elif placar_grenal[0] < placar_grenal[1]:
        vitorias_gremio += 1
    else:
        empates += 1

    grenais += 1

    if int(input("Novo grenal (1-sim 2-nao)\n")) == 2:
        break

print(f"{grenais} grenais")
print(f"Inter:{vitorias_inter}")
print(f"Gremio:{vitorias_gremio}")
print(f"Empates:{empates}")

if vitorias_inter > vitorias_gremio:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")
