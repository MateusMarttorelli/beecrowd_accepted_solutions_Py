alimentos = {
    "suco de laranja": 120,
    "morango fresco": 85,
    "mamao": 85,
    "goiaba vermelha": 70,
    "manga": 56,
    "laranja": 50,
    "brocolis": 34
}

while True:
    n = int(input())
    if n == 0:
        break

    total = 0

    for _ in range(n):
        quantidade, alimento = input().split(maxsplit=1)
        total += int(quantidade) * alimentos[alimento]

    if total < 110:
        print(f"Mais {110 - total} mg")
    elif total > 130:
        print(f"Menos {total - 130} mg")
    else:
        print(f"{total} mg")

