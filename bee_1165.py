n = int(input())

for i in range(n):
    numero_primo = True
    x = int(input())

    for j in range(2, (x//2)+1):
        if x % j == 0:
            numero_primo = False

    if numero_primo:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
