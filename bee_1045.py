<<<<<<< HEAD
a, b, c = sorted(map(float, input().split()), reverse=True)

if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if pow(a, 2) == (pow(b, 2) + pow(c, 2)):
        print('TRIANGULO RETANGULO')
    if pow(a, 2) > (pow(b, 2) + pow(c, 2)):
        print('TRIANGULO OBTUSANGULO')
    if pow(a, 2) < (pow(b, 2) + pow(c, 2)):
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
=======
a, b, c = sorted(map(float, input().split()), reverse=True)

if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if pow(a, 2) == (pow(b, 2) + pow(c, 2)):
        print('TRIANGULO RETANGULO')
    if pow(a, 2) > (pow(b, 2) + pow(c, 2)):
        print('TRIANGULO OBTUSANGULO')
    if pow(a, 2) < (pow(b, 2) + pow(c, 2)):
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
>>>>>>> bd57b8c5326bf8b105bee14a09bba34eb6cf4770
