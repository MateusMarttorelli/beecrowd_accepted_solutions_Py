saida, tempo_de_viagem, fuso = map(int, input().split())

horario_de_chegada = saida + tempo_de_viagem + fuso

if horario_de_chegada >= 24:
    horario_de_chegada -= 24
elif horario_de_chegada < 0:
    horario_de_chegada += 24

print(horario_de_chegada)