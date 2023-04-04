h_inicial, h_final = map(int, input().split())

if h_inicial < h_final:
    h_total = h_final - h_inicial
else:
    h_total = (24 - h_inicial) + h_final

print(f'O JOGO DUROU {h_total} HORA(S)')
