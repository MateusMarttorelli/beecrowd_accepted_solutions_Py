while True:
    x = int(input())

    if x == 0:
        break
    else:
        for i in range(1, x+1):
            print(i, end='')
            if i == x:
                print()
            else:
                print(end=' ')
