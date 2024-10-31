from datetime import time

casos_de_teste = int(input())

for _ in range(casos_de_teste):
    horas, minutos, acao_porta = map(int, input().split())

    horario = time(horas, minutos)

    print(f"{horario.strftime('%H:%M')} - {'A porta abriu!' if acao_porta == 1 else 'A porta fechou!'}")
