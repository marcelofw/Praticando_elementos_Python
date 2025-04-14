# idade = int(input("Qual é a sua idade? "))
# maioridade = "adulto" if idade >= 18 else "menor de idade"
# print(f"A pessoa de {idade} anos de idade é {maioridade}.")

# media = int(input("Qual é a média das suas notas? "))
# status = "aprovado com louvor" if media >= 9 else "aprovado" if media >=7 else "reprovado"
# print(f"Com a média {media} você foi {status}.")

# num = int(input("Insira um número: "))
# status = "par" if num % 2 == 0 else "ímpar"
# print(f"O número é {status}.")

# nome = input("Qual é seu nome? ")
# status = nome if nome else "Usuário anônimo"
# print(f"Olá, {status}.")

cliente_vip = input("Você é cliente vip? (sim/não)").lower().strip()
mensagem = "Desconto de 10% aplicado!" if cliente_vip == "sim" else "Sem descontos, infelizmente."
print(mensagem)