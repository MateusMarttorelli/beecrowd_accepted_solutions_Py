import math

n = int(input())

limite_inferior = n / math.log(n)
limite_superior = 1.25506 * (n / math.log(n))

print(f"{limite_inferior:.1f} {limite_superior:.1f}")
