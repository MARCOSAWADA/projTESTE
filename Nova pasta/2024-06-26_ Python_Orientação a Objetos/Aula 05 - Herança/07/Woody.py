from Brinquedos import Brinquedos

class Woody(Brinquedos):
    def __init__(self, cor, tamanho, preco):
        super().__init__(nome="Woody", cor=cor, tamanho=tamanho, preco=preco)

    def laca(self):
        print(f"{self.nome} está LAÇANDO !!!!!")