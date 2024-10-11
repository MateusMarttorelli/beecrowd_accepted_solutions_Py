n_alunos = int(input())
matricula_melhor_aluno = ""
maior_nota = 0.0

for _ in range(n_alunos):
    matricula, nota = input().split()
    nota = float(nota)

    if nota > maior_nota:
        maior_nota = nota
        matricula_melhor_aluno = matricula

if maior_nota >= 8:
    print(matricula_melhor_aluno)
else:
    print("Minimum note not reached")