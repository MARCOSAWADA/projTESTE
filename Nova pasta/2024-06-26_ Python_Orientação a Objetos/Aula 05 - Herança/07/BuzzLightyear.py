from Brinquedos import Brinquedos

class BuzzLightyear(Brinquedos):
    def __init__(self, cor, tamanho, preco):
        super().__init__(nome="Buzz Lightyear", cor=cor, tamanho=tamanho, preco=preco)

    def voar(self):
        print(f"{self.nome} está VOANDO !!!!!")
