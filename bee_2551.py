while True:
    try:
        n = int(input())
        recorde_vm = 0

        for i in range(1, n + 1):
            t, d = map(int, input().split())
            vm = d / t

            if vm > recorde_vm:
                recorde_vm = vm
                print(i)

    except EOFError:
        break
