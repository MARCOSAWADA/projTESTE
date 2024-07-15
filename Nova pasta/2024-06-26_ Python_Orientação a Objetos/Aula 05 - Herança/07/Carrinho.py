from Brinquedos import Brinquedos

class Carrinho(Brinquedos):
    def __init__(self, cor, tamanho, preco):
        super().__init__(nome="Carrinho", cor=cor, tamanho=tamanho, preco=preco)

    def correr(self):
        print(f"O {self.nome} está correndo em ALTA VELOCIDADE !!!!.")