while True:
    nota1 = float(input())

    if nota1 < 0 or nota1 > 10:
        print("nota invalida")
        continue
    else:
        break

while True:
    nota2 = float(input())

    if nota2 < 0 or nota2 > 10:
        print("nota invalida")
        continue
    else:
        break

media = (nota1 + nota2) / 2
print(f"media = {media:.2f}")
