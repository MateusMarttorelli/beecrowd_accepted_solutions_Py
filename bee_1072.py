var_in = 0
var_out = 0

n = int(input())

for i in range(n):
    x = int(input())

    if 10 <= x <= 20:
        var_in = var_in + 1
    else:
        var_out = var_out + 1

print(var_in, "in")
print(var_out, "out")
