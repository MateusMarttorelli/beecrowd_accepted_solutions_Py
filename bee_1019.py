tempo_em_segundos = {'hora': 3600, 'minuto': 60, 'segundo': 1}

tempo_total = int(input())

for i, j in tempo_em_segundos.items():
    tempo_em_segundos[i] = tempo_total//j
    tempo_total -= tempo_em_segundos[i]*j

print(f'{tempo_em_segundos["hora"]}:{tempo_em_segundos["minuto"]}:{tempo_em_segundos["segundo"]}')
