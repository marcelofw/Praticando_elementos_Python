num_alunos = int(input("Quantos alunos estão na classe? "))
alunos_e_notas = []

for aluno in range(num_alunos):
    print(f"Dados do aluno {aluno + 1}")
    nome = input("Nome: ")
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
    alunos_e_notas.append((nome, (nota1, nota2, nota3)))
    print(alunos_e_notas)

for nome, notas in alunos_e_notas:
    media = sum(notas) / len(notas)
    status = "Aprovado" if media >=7 else "Reprovado"
    print(f"A média das notas de {nome} é {media: .2f} e o aluno foi {status}.")

# for nome, notas in alunos_e_notas:
#     media = sum(notas) / len(notas)
#     if media >=7:
#         print(f"A média das notas de {nome} é {media: .2f} e o aluno foi Aprovado.")
#     else:
#         print(f"A média das notas de {nome} é {media: .2f} e o aluno foi Reprovado.")
