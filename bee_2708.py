turistas_restantes = 0
jeeps_restantes = 0

while True:
    entrada = input()

    if entrada == "ABEND":
        break

    sentido, turistas = entrada.split()
    turistas = int(turistas)

    if sentido == "SALIDA":
        turistas_restantes += turistas
        jeeps_restantes += 1
    else:
        turistas_restantes -= turistas
        jeeps_restantes -= 1

print(turistas_restantes)
print(jeeps_restantes)





