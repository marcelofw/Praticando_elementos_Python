def eh_primo(n):        
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

num_teste = int(input("Qual número você gostaria de saber se é primo? "))

if eh_primo(num_teste) == True:
    print("O número é primo.")
else:
    print("O número não é primo.")
