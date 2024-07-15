# 1 - Classe Pessoa: Crie uma classe que modele uma pessoa. Esta classe deve possuir os seguintes atributos:​
# Nome​
# Idade​
# Endereço​

# A classe deve ter os seguintes métodos:​
# Mostrar nome;​
# Alterar a idade;​
# Imprimir endereço.​

class Pessoa:
    def __init__(self,nome,idade,id):
        self.nome = nome
        self.idade = idade
        self.id = id

    def getNome(self):
        return self.nome
    
    def setIdade(self,novaIdade):
        self.idade = novaIdade


pessoa1 = Pessoa(1, "Wendril", 18)

print(pessoa1.id)
print(pessoa1.getNome())
print(pessoa1.idade)
print("####"*8)
#### SETAR -> ALTERAR -> EDITAR
pessoa1.setIdade(23)
print(pessoa1.idade)