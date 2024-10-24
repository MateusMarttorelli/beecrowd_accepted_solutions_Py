casos_de_teste = int(input())

for _ in range(casos_de_teste):
    palavra = input()
    milisegundos = len(palavra)
    print(f"{0.01 * milisegundos:.2f}")