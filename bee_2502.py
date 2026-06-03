while True:
    try:
        tamanho_cifra, n_frases = map(int, input().split())
        cifra_01 = input()
        cifra_02 = input()

        mapa = {}
        for a, b in zip(cifra_01, cifra_02):
            mapa[a] = b
            mapa[b] = a
            mapa[a.lower()] = b.lower()
            mapa[b.lower()] = a.lower()

        for _ in range(n_frases):
            frase_cifrada = input()
            frase_decifrada = ""

            for c in frase_cifrada:
                frase_decifrada += mapa.get(c, c)

            print(frase_decifrada)

        print()

    except EOFError:
        break
