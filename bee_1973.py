n_estrelas = int(input())
carneiros_em_estrelas = list(map(int, input().split()))

estrelas = [[carneiros, False] for carneiros in carneiros_em_estrelas]

posicao = 0

while 0 <= posicao < n_estrelas:
    carneiros_inicialmente_na_estrela = estrelas[posicao][0]

    if carneiros_inicialmente_na_estrela > 0:
        estrelas[posicao][0] -= 1
        estrelas[posicao][1] = True

    # Atualiza a posição
    posicao += 1 if carneiros_inicialmente_na_estrela % 2 else -1

# Conta as estrelas atacadas e os carneiros não roubados
n_estrelas_atacadas = sum(1 for estrela in estrelas if estrela[1])
n_carneiros_nao_roubados = sum(estrela[0] for estrela in estrelas)

print(f"{n_estrelas_atacadas} {n_carneiros_nao_roubados}")
