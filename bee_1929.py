from itertools import combinations

varetas = list(map(int, input().split()))

existencia_de_triangulo = any(a < b + c and b < a + c and c < a + b for a, b, c in combinations(varetas, 3))

if existencia_de_triangulo:
    print('S')
else:
    print('N')
