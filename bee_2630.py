ops = {
            "eye": lambda r, g, b: int(0.3 * r + 0.59 * g + 0.11 * b),
            "min": lambda r, g, b: min(r, g, b),
            "max": lambda r, g, b: max(r, g, b),
            "mean": lambda r, g, b: (r + g + b) // 3
        }

while True:
    try:
        n = int(input())

        for i in range(1, n + 1):
            abordagem = input().strip()
            r, g, b = map(int, input().split())

            p = ops[abordagem](r, g, b)

            print(f"Caso #{i}: {p}")

    except EOFError:
        break
