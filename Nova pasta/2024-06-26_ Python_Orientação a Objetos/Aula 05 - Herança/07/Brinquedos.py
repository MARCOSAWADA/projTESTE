# Classe Brinquedos: Andy Davis precisa classificar seus brinquedos por Subclasses, 
# sabemos que cada brinquedo tem atributos e métodos diferentes, exemplo Buzz Lightyear voa e Woody laça. 
# Defina principais atributos:​
# Nome, Cor, Tamanho, Preço;​

# Método:​
# brincar(); - fazer um print simples, estou brincando com {nome do brinquedo}​

# Subclasses:​
# Crie 10 sub classes de brinquedos com seus respectivos atributos e métodos.​

# Utilize o polimorfismo para reescrever o método herdado da super classe​

class Brinquedos:
    def __init__ (self, nome, cor, tamanho, preco):
        self. nome = nome
        self. cor = cor
        self. tamanho = tamanho
        self. preco = preco

    def brincar(self):
        print(f"Estou brincando com {self.nome}.")
