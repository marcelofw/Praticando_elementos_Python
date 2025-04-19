# try:
#     resultado = 10 / 0
# except ZeroDivisionError:
#     print("Não é possível dividir por zero.")

# try:
#     x = int("abc")
# except Exception as erro:
#     print(f"Ocorreu um erro: {erro}")

# try:
#     lista = [1, 2, 3]
#     print(lista[5])
#     print(1/0)
# except IndexError:
#     print("Índice fora da lista.")
# except ZeroDivisionError:
#     print("Divisão por zero.")

# try:
#     numero = int(input("Digite um número: "))
# except ValueError:
#     print("Por favor, digite um número válido.")
# else:
#     print(f"Você digitou: {numero}")
# finally:                              
#     print("Fim da execução.")

def dividir(a, b):
    if b == 0:
        raise ValueError("O denominador não pode ser zero.")
    return a / b
try:
    print(dividir(10, 0))
except ValueError as erro:
    print("Erro personalizado: ", erro)