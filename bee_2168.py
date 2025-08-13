n = int(input())

portland = []
for _ in range(n + 1):
    portland.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        cameras = (portland[i][j] + portland[i][j+1] +
                   portland[i+1][j] + portland[i+1][j+1])
        if cameras >= 2:
            print('S', end='')
        else:
            print('U', end='')
    print()
