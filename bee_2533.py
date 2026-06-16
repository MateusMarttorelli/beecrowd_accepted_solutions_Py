while True:
    try:
        n = int(input())
        soma = 0
        carga_total = 0

        for _ in range(n):
            nota, carga = map(int, input().split())
            soma += nota * carga
            carga_total += carga

        resultado = soma / (carga_total * 100)
        print(f"{resultado:.4f}")

    except EOFError:
        break