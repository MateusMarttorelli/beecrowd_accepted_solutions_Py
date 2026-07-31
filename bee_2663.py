import heapq

n = int(input())
k = int(input())

notas = [int(input()) for _ in range(n)]

# k maiores notas, sem ordenar toda a lista
k_maiores = heapq.nlargest(k, notas)

nota_ultimo_colocado = k_maiores[-1]

# conta quantas notas são >= à nota do k-ésimo colocado
resultado = sum(nota >= nota_ultimo_colocado for nota in notas)

print(resultado)
