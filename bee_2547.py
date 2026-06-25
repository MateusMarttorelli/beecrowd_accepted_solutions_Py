while True:
    try:
        n, alt_min, alt_max = map(int, input().split())
        ok = sum(alt_min <= int(input()) <= alt_max for _ in range(n))
        print(ok)

    except EOFError:
        break
