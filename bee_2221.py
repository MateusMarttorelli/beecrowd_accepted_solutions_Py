def calcular_golpe(a, d, l, bonus):
    golpe = (a + d) / 2
    if l % 2 == 0:
        golpe += bonus
    return golpe

n = int(input())

for _ in range(n):
    bonus = int(input())
    a1, d1, l1 = map(int, input().split())
    a2, d2, l2 = map(int, input().split())

    golpe_dabriel = calcular_golpe(a1, d1, l1, bonus)
    golpe_guarte = calcular_golpe(a2, d2, l2, bonus)

    if golpe_dabriel > golpe_guarte:
        print("Dabriel")
    elif golpe_guarte > golpe_dabriel:
        print("Guarte")
    else:
        print("Empate")
