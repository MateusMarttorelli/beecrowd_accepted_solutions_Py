from datetime import datetime, timedelta

while True:
    try:
        entrada = input().strip()

        hora_acordou = datetime.strptime(entrada, '%H:%M')

        horario_encontro = datetime.strptime('08:00', '%H:%M')

        tempo_chegada = timedelta(minutes=60)

        hora_chegada = hora_acordou + tempo_chegada
        if hora_chegada > horario_encontro:
            atraso = int((hora_chegada - horario_encontro).total_seconds() // 60)
        else:
            atraso = 0

        print(f"Atraso maximo: {atraso}")

    except EOFError:
        break