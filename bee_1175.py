N = []

for i in range(20):
    N.append(int(input()))

for i in range(10):
    N[i], N[19 - i] = N[19 - i], N[i]

for i, j in enumerate(N):
    print(f"N[{i}] = {j}")
