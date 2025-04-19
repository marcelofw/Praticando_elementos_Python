# class Monitores():
#     def __init__(self, marca, tamanho, resolucao):
#         self.marca = marca
#         self.tamanho = tamanho
#         self.resolucao = resolucao

#     def imprimir_detalhes(self):         
#         print("Marca:", self.marca)
#         print("Tamanho:", self.tamanho)
#         print("Resolução:", self.resolucao)

#     def alterar_resolucao(self, nova_resolucao):
#         self.resolucao = nova_resolucao
#         print("Resolução atualizada para:", self.resolucao)

# Monitor1 = Monitores("LG", '24"', "Full HD")
# Monitor1.imprimir_detalhes()
# Monitor1.alterar_resolucao("4K")

#-------------------------------------------------------------------------------------

# class Dispositivo:                  
#     def __init__(self, marca):
#         self.marca = marca

#     def ligar(self):
#         print(f"{self.marca} ligado.")

# class Monitor(Dispositivo):         
#     def __init__(self, marca, tamanho):
#         super().__init__(marca)                 #essa linha equivale a: Dispositivo.__init__(self, marca)
#         self.tamanho = tamanho

#     def mostrar_resolucao(self, resolucao):
#         print(f"A resolução do monitor é: {resolucao}")

# Monitor1 = Monitor("LG", 27)
# Monitor1.ligar()
# Monitor1.mostrar_resolucao("4K")

#----------------------------------------------------------------------------------------

class Animal:
    def emitir_som(self):
        print("O animal emite um som.")

class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro late: au au!")

class Gato(Animal):
    def emitir_som(self):
        print("O gato mia: miau!")

animais = [Cachorro(), Gato(), Animal()]
for animal in animais:
    animal.emitir_som()
















