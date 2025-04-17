# nomes = ["Ana", "Bruno", "Carlos"]
# idades = [25, 30, 22]
# profissoes = ["médica", "advogado", "engenheiro"]

# combinados = zip(nomes, idades, profissoes)
# print(list(combinados))


# chaves = ["nome", "idade", "cidade"]
# valores = ["Alice", "28", "São Paulo"]
# dicionario = dict(zip(chaves, valores))
# print(dicionario)


# a = [1, 2, 3]
# b = ["a", "b"]
# print(list(zip(a, b)))


pares = [(1, "a"), (2, "b"), (3, "c")]
nums, letras = zip(*pares)
print(nums)
print(letras)