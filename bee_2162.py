n = int(input())
alturas = list(map(int, input().split()))
pico_ou_vale = -1
valido = True

for i in range(1, len(alturas)):

    if pico_ou_vale == -1:
        if alturas[i] > alturas[i-1]:
            pico_ou_vale = 1
        else:
            pico_ou_vale = 0

    elif pico_ou_vale == 1 and alturas[i] > alturas[i-1]:
        valido = False
        break

    elif pico_ou_vale == 0 and alturas[i] < alturas[i-1]:
        valido = False
        break

    else:
        if alturas[i] > alturas[i-1]:
            pico_ou_vale = 1
        else:
            pico_ou_vale = 0

if valido:
    print(1)
else:
    print(0)
