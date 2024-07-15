class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        
    def mostrar_nome(self):
        return self.nome
        
    def alterar_idade(self,novaIdade):
        self.idade = novaIdade
        print(f"Idade alterada para: {self.idade}")
        
    def imprimir_endereco(self):
        print(f"Endereço: {self.endereco}")
        
        
pessoa1 = Pessoa("MKS", 35 ,"Oyama-Shi, 123")

print(f"Nome da pessoa: {pessoa1.mostrar_nome()}")
print(f"Idade da pessoa: {pessoa1.idade}")

pessoa1.alterar_idade(30)
print(f"Idade atualizada da pessoa: {pessoa1.idade}")
pessoa1.imprimir_endereco()
