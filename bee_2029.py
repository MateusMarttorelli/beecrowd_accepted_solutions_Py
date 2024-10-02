while True:
    try:
        volume = float(input())
        diametro = float(input())

        PI = 3.14
        raio = diametro/2.0
        area_da_base = PI * raio**2
        altura = volume / area_da_base

        print(f"ALTURA = {altura:.2f}")
        print(f"AREA = {area_da_base:.2f}")

    except EOFError:
        break