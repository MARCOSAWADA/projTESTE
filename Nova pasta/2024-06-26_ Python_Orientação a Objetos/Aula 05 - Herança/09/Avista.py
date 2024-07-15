from Compra import Compra

class Avista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto

    def preco_com_desconto(self):
        return self.valor_total - self.desconto