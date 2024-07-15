from Passagem import Passagem

class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portaodeembarque, checkin):
        super().__init__(preco, assento)
        self.portaodeembarque = portaodeembarque
        self.checkin = checkin

    def decolar(self):
        print(f"O avião está decolando pelo portão de embarque {self.portaodeembarque}.")