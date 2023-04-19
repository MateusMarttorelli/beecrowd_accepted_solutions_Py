dia_inicial = int(input().split()[1])
hora_inicial, minuto_inicial, segundo_inicial = map(int, input().split(' : '))
dia_final = int(input().split()[1])
hora_final, minuto_final, segundo_final = map(int, input().split(' : '))

tempo_inicial_em_segundos = (dia_inicial * 86400) + (hora_inicial * 3600)\
                            + (minuto_inicial * 60) + segundo_inicial

tempo_final_em_segundos = (dia_final * 86400) + (hora_final * 3600)\
                            + (minuto_final * 60) + segundo_final

tempo_total_em_segundos = tempo_final_em_segundos - tempo_inicial_em_segundos

dias = tempo_total_em_segundos // 86400
tempo_total_em_segundos -= (dias*86400)

horas = tempo_total_em_segundos // 3600
tempo_total_em_segundos -= (horas*3600)

minutos = tempo_total_em_segundos // 60
tempo_total_em_segundos -= (minutos*60)

segundos = tempo_total_em_segundos

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
