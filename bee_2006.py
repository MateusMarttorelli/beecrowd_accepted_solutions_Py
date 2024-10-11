cha = int(input())
suposicoes = list(map(int, input().split()))

suposicoes_certas = suposicoes.count(cha)
print(suposicoes_certas)