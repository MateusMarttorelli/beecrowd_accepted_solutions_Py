import math

n = int(input())

x = (1 + math.sqrt(5)) / 2.0
y = (1 - math.sqrt(5)) / 2.0

fibonacci = (pow(x, n) - pow(y, n)) / math.sqrt(5)

print(f"{fibonacci:.1f}")
