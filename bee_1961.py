altura_pulo, n_canos = map(int, input().split())
canos = list(map(int, input().split()))

resultado = "YOU WIN"

for i in range(1, n_canos):
    if abs(canos[i] - canos[i - 1]) > altura_pulo:
        resultado = "GAME OVER"
        break

print(resultado)

