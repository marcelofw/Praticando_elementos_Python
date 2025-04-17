from functools import reduce

# numeros = [1, 2, 3, 4, 5]

# def somar(x, y):
#     return x + y

# resultado = reduce(somar, numeros)
# print(resultado)
# resultado = reduce(lambda x, y: x + y, numeros)
# print(resultado)


# numeros = [1, 2, 3, 4]
# resultado = reduce(lambda x, y: x * y, numeros)
# print(resultado)


numeros = [4, 2, 8, 6]
resultado = reduce(lambda x, y: x if x > y else y, numeros)
print(resultado)
