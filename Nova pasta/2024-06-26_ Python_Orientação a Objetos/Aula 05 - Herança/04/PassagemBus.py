from Passagem import Passagem

class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self):
        print(f"Abastecendo o ônibus com placa {self.placa}.")