n = int(input())

totais = [0, 0, 0]
totais_ok = [0, 0, 0]

for _ in range(n):
    input()
    tentativas = list(map(int, input().split()))
    acertos = list(map(int, input().split()))

    totais = [t + nt for t, nt in zip(totais, tentativas)]
    totais_ok = [t + nok for t, nok in zip(totais_ok, acertos)]

nomes = ["Saque", "Bloqueio", "Ataque"]
for nome, total, ok in zip(nomes, totais, totais_ok):
    print(f"Pontos de {nome}: {(ok / total) * 100:.2f} %.")

