# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

#     def ligar(self):
#         print("\n Seu veículo ligou", self.marca, self.modelo, self.ano)

# class SmartCar(Carro):
#     def localizar(self):
#         print(f"\n A {self.marca} está localizado em joão pessoa")

# meu_carro = Carro("Chevrolet", "Onix", 2017)
# meu_carro.ligar()

# carro_smart = SmartCar("BMW", "Sport", 2024)
# carro_smart.ligar()
# carro_smart.localizar()

#ex1 crie duas classe (animal e som) e faça uma relaçao entre eles

class Animal:
    def __init__(self, tipo, nome, porte, idade):
        self.tipo = tipo
        self.nome = nome
        self.porte = porte
        self.idade = idade
        
    
    def acao(self):
        print(f"Seu {self.tipo} tem o nome de {self.nome}, é de {self.porte} porte e tem {self.idade} anos")
    
class Cachorro(Animal):
    def latir(self):
        print("O cachorro late")

class Gato(Animal):
    def mia(self):
        print("O gato mia")

meuCachorro = Cachorro('cachorro', 'Kleriton', 'médio', 3)
MeuGato = Gato('gato', 'Biel', 'pequeno', 5)

meuCachorro.acao()
meuCachorro.latir()
MeuGato.acao()
MeuGato.mia()