
def avaliar_aluno(nome, nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        situacao = "Aprovado"
    elif media >=5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    return f"{nome} - Média: {media: .2f} - Situação: {situacao}"

nome = input("Insira o nome do aluno(a): ")
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

resultado = avaliar_aluno(nome, nota1, nota2, nota3)
print(resultado)



