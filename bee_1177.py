t = int(input())
n = list()

for i in range(1000):
    n.append(i % t)

for i, j in enumerate(n):
    print(f"N[{i}] = {j}")
