i = 1
j = 7

while i <= 9:

    while j >= i+4:
        print(f"I={i} J={j}")
        j -= 1

    i += 2
    j = i + 6
