V = int(input())

N = [V * (2 ** i) for i in range(10)]

for i in range(10):
    print(f"N[{i}] = {N[i]}")
