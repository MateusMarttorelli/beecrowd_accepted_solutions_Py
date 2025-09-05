n = int(input())

for _ in range(n):
    competidor = input()
    dificuldade = float(input())
    notas = list(map(float, input().split()))

    resultado = (sum(notas) - max(notas) - min(notas)) * dificuldade

    print(f"{competidor} {resultado:.2f}")