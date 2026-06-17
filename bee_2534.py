import sys

for line in sys.stdin:
    n, q = map(int, line.split())
    notas = [int(sys.stdin.readline()) for _ in range(n)]
    notas.sort(reverse=True)

    for _ in range(q):
        idx = int(sys.stdin.readline())
        print(notas[idx - 1])