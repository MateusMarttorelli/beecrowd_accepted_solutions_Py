while True:
    try:
        while True:
            n = int(input())
            palavras_pesquisadas = [input().strip() for _ in range(n)]

            q = int(input())

            for _ in range(q):
                consulta = input().strip()

                match_palavras = 0
                tamanho_maior_palavra = 0

                for palavra in palavras_pesquisadas:
                    if palavra.startswith(consulta):  # prefixo
                        match_palavras += 1
                        tamanho_palavra = len(palavra)
                        if tamanho_palavra > tamanho_maior_palavra:
                            tamanho_maior_palavra = tamanho_palavra

                if tamanho_maior_palavra == 0:
                    print("-1")
                else:
                    print(match_palavras, tamanho_maior_palavra)

    except EOFError:
        break

