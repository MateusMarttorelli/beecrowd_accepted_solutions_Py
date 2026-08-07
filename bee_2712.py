n = int(input())

for _ in range(n):
    placa = input()

    # Verificação estrutural básica
    if len(placa) != 8 or placa[3] != '-' or not placa[:3].isalpha() or not placa[:3].isupper() or not placa[4:].isnumeric():
        print("FAILURE")
        continue

    # Último dígito como inteiro
    ultimo = int(placa[-1])

    # Mapeamento dos dias
    dias = {
        (1, 2): "MONDAY",
        (3, 4): "TUESDAY",
        (5, 6): "WEDNESDAY",
        (7, 8): "THURSDAY",
        (9, 0): "FRIDAY"
    }

    # Encontrar o dia correspondente
    for numeros, dia in dias.items():
        if ultimo in numeros:
            print(dia)
            break
