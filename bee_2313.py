a, b, c = sorted(map(int, input().split()))

if a + b <= c:
    print("Invalido")

else:
    if a == b == c:
        tipo = "Equilatero"
    elif a == b or a == c or b == c:
        tipo = "Isoceles"
    else:
        tipo = "Escaleno"

    print(f"Valido-{tipo}")

    if c**2 == a**2 + b**2:
        print("Retangulo: S")
    else:
        print("Retangulo: N")
