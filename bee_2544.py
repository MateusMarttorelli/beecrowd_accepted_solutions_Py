import math

while True:
    try:
        n = int(input())
        print(int(math.log2(n)))

    except EOFError:
        break
