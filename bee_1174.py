A = []

for i in range(100):
    A.append(float(input()))

for i, j in enumerate(A):
    if j <= 10:
        print(f"A[{i}] = {j}")
