x, y = map(int, input().split())

aux = 1

while aux <= y:

    for i in range(x):
        print(f"{aux}", end='')
        aux += 1

        if i == x-1:
            print()
        else:
            print(end=' ')

        if aux > y:
            break
