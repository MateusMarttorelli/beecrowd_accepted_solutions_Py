n = list()
n.append(float(input()))

for i in range(1, 100):
    n.append(n[i-1] / 2.0)

for i, j in enumerate(n):
    print(f"N[{i}] = {j:.4f}")
