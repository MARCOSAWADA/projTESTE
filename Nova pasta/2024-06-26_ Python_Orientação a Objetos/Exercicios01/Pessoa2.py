class Pessoa2:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        
    def mostrar_nome(self):
        return self.nome
    def alterar_idade(self,novaIdade):
        self.idade = novaIdade
        
x = Pessoa2("aula", 10 ,"bandeirantes")
print("Mostre o nome")
print(x.nome)

print("-"*50)
print("idade antiga ")
print(x.idade)
print("-"*50)
x.alterar_idade(int(input("Agora digite uma nova idade para ser alterada: ")))
print("-"*50)
print("a nova idade alterada é: ")

print(x.idade)

print("-"*50)
print("Imprime o endereço")
print(x.endereco)