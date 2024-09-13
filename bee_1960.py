numero = int(input())

numeros_romanos = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
        (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
        (5, 'V'), (4, 'IV'), (1, 'I')
    ]

resultado = []

for valor, numeral in numeros_romanos:
    while numero >= valor:
        resultado.append(numeral)
        numero -= valor

print("".join(resultado))
