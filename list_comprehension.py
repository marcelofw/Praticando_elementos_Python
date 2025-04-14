# numeros = [x for x in range(10)]
# print(numeros)

# numeros = []
# for x in range(10):
#     numeros.append(x)
# print(numeros)
# ----------------------------------------------

# quadrados = [x**2 for x in range(10)]
# print(quadrados)

# quadrados = []
# for x in range(10):
#     potencia = x ** 2
#     quadrados.append(potencia)
# print(quadrados)
# ----------------------------------------------

# pares = [x for x in range(20) if x % 2 == 0]
# print(pares)

# pares = []
# for x in range(20):
#     if x % 2 == 0:
#         pares.append(x)
# print(pares)
# ----------------------------------------------

# palavras = ["aprender", "python", "é", "legal"]
# maiusculas = [palavra.upper() for palavra in palavras]
# print(maiusculas)

# palavras = ["aprender", "python", "é", "legal"]
# maiusculas = []
# for palavra in palavras:
#     maiusculas.append(palavra.upper())
# print(maiusculas)
# ----------------------------------------------

# tuplas = [(x, x ** 2) for x in range(5)]
# print(tuplas)

# tuplas = []
# for x in range(5):
#     operacao = (x, x ** 2)
#     tuplas.append(operacao)
# print(tuplas)
# ----------------------------------------------

# palavras = [" aprender ", " python", " é  ", " legal "]
# limpar_espacos = [palavra.strip() for palavra in palavras]
# print(limpar_espacos)

# limpar_espacos = []
# palavras = [" aprender ", " python", " é  ", " legal "]
# for palavra in palavras:
#     limpar_espacos.append(palavra.strip())
# print(limpar_espacos)
# ----------------------------------------------

# par_ou_impar = ["par" if x % 2 == 0 else "impar" for x in range(5)]
# print(par_ou_impar)

par_ou_impar = []
for x in range(5):
    if x % 2 == 0:
        par_ou_impar.append("par")
    else:
        par_ou_impar.append("impar")
print(par_ou_impar)