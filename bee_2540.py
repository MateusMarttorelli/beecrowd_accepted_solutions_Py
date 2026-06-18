import math

while True:
    try:
        n = int(input())
        votos = list(map(int, input().split()))
        favoraveis = votos.count(1)

        if favoraveis >= math.ceil(2 * n / 3):
            print("impeachment")
        else:
            print("acusacao arquivada")
            
    except EOFError:
        break

