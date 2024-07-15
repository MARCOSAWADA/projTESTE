from Compra import Compra

class Parcelada(Compra):
    def __init__(self, numero, produto, valor, numero_de_parcelas):
        super().__init__(numero, produto, valor)
        self.numero_de_parcelas = numero_de_parcelas

    def valor_das_parcelas(self):
        return self.valor_total / self.numero_de_parcelas