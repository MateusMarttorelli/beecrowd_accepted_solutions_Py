n = int(input())

for i in range(n):
    x1, x2, x3 = map(float, input().split())
    media = (2*x1 + 3*x2 + 5*x3) / 10
    print(round(media, 1))
