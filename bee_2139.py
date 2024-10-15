from datetime import date

try:
    while True:
        mes, dia = map(int, input().split())
        data_fornecida = date(2016, mes, dia)
        data_do_natal = date(2016, 12, 25)
        tempo_para_natal = data_do_natal - data_fornecida

        if tempo_para_natal.days < 0:
            print("Ja passou!")
        elif tempo_para_natal.days == 0:
            print("E natal!")
        elif tempo_para_natal.days == 1:
            print("E vespera de natal!")
        else:
            print(f"Faltam {tempo_para_natal.days} dias para o natal!")

except EOFError:
    pass