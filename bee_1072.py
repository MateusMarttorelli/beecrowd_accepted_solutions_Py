n = int(input())
num_in = 0
num_out = 0

for num in range(n):
    x = int(input())

    if 20 >= x >= 10:
        num_in += 1
    else:
        num_out += 1

print(f"{num_in} in")
print(f"{num_out} out")




