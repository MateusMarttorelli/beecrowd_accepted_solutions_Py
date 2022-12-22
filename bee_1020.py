tempo_em_dias = {'ano': 365, 'mes': 30, 'dia': 1}

tempo_total = int(input())

for i, j in tempo_em_dias.items():
    tempo_em_dias[i] = tempo_total//j
    tempo_total -= tempo_em_dias[i]*j

print(f'{tempo_em_dias["ano"]} ano(s)')
print(f'{tempo_em_dias["mes"]} mes(es)')
print(f'{tempo_em_dias["dia"]} dia(s)')
