soma_das_idades = 0
n_idades = 0

while True:
    idade = int(input())

    if idade < 0:
        break
    else:
        soma_das_idades += idade
        n_idades += 1

media = soma_das_idades / n_idades
print(f"{media:.2f}")
