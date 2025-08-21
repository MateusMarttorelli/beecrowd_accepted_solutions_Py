from math import dist

while True:
    try:
        xf, yf, xi, yi, vi, r1, r2 = list(map(int, input().split()))

        distancia_inicial = dist((xf, yf), (xi, yi))
        distancia_final = distancia_inicial + (vi * 1.5)

        if distancia_final <= r1 + r2:
            print("Y")
        else:
            print("N")

    except EOFError:
        break
