n = int(input())

if n == 1:
    print("0")
elif n == 2:
    print("0 1")
else:
    aux1 = 0
    aux2 = 1

    print("0 1", end=' ')

    for i in range(n-2):
        if i == (n-3):
            print(aux1 + aux2)
        else:
            print(aux1 + aux2, end=' ')

        aux1, aux2 = aux2, (aux1 + aux2)
