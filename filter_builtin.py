# numeros = [1, 2, 3, 4, 5, 6]
# pares = filter(lambda x: x % 2 == 0, numeros)
# print(list(pares))

# palavras = ["sol", "lua", "estrela", "céu", "planeta"]
# longas = filter(lambda palavra: len(palavra) > 3, palavras)
# print(list(longas))

# valores = [0, 1, "", "Python", False, True, None]
# filtrados = filter(None, valores)
# print(list(filtrados))              

# nomes = ["Ana", "", "Lucas", "", "Maria"]
# limpos = filter(lambda nome: nome != "", nomes)
# print(list(limpos))

def eh_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6]
pares = filter(eh_par, numeros)
print(list(pares))