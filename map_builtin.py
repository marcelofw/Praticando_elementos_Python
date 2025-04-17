# numeros = [1, 2, 3, 4]
# dobrados = list(map(lambda x: x * 2, numeros))  #os argumentos passados ao método ou função built-in "map" foram uma função anônima e uma lista
# print(dobrados)

# palavras = ["gato", "cachorro", "pássaro"]
# maiusculas = list(map(lambda p: p.upper(), palavras))
# print(maiusculas)

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# somas = list(map(lambda x,y: x + y, lista1, lista2))
# print(somas)

palavras = ["maçã", "banana", "uva"]
tamanhos = list(map(lambda p: len(p), palavras))
print(tamanhos)