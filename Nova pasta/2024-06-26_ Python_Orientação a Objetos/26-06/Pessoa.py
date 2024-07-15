class Pessoa:
    def __init__(self,id=0,nome=""):
        self.id = id
        self.nome = nome

    def hello(self):
        print(f"Olá {self.nome}")


pes1= Pessoa()

print(pes1.id)

print("BOM DIA")
name = input("Digite seu nome: ")

pes1.nome = name

pes1.hello()