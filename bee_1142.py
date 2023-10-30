n = int(input())
aux = 1

for i in range(1, n+1):
    for j in range(3):

        print(f"{aux+j}", end=' ')

    print("PUM")

    aux += 4
