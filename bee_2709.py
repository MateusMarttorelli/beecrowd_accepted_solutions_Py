def isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

while True:
    try:
        m = int(input())
        moedas = [int(input()) for _ in range(m)]
        salto = int(input())

        # soma do topo para baixo
        resultado = sum(moedas[::-salto])

        if isprime(resultado):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")

    except EOFError:
        break

