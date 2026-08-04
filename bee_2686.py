while True:
    try:
        grau = float(input())

        # Converte grau para segundos do dia
        momento_do_dia = grau * 240  # 86400 / 360 = 240

        hora = int(momento_do_dia // 3600)
        minuto = int((momento_do_dia % 3600) // 60)
        segundo = int(momento_do_dia % 60)

        # Ajuste de fuso (6 horas)
        hora = (hora + 6) % 24

        horario_formatado = f"{hora:02d}:{minuto:02d}:{segundo:02d}"

        if 6 <= hora < 12:
            print("Bom Dia!!")
            print(horario_formatado)
        elif 12 <= hora < 18:
            print("Boa Tarde!!")
            print(horario_formatado)
        elif 18 <= hora < 24:
            print("Boa Noite!!")
            print(horario_formatado)
        else:
            print("De Madrugada!!")
            print(horario_formatado)

    except EOFError:
        break
