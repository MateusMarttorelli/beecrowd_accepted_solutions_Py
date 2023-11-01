n = int(input())

for i in range(1, n+1):
    for j in range(2):

        print(f"{i}", end=' ')
        print(f"{pow(i, 2) + j}", end=' ')
        print(f"{pow(i, 3) + j}")
