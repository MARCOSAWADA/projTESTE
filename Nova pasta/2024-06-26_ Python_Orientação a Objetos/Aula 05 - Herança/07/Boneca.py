from Brinquedos import Brinquedos

class Boneca(Brinquedos):
    def __init__(self, cor, tamanho, preco):
        super().__init__(nome="Boneca", cor=cor, tamanho=tamanho, preco=preco)

    def pentear_cabelo(self):
        print(f"Estamos penteando o cabelo da {self.nome}.")