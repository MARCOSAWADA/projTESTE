from Ingresso import Ingresso

class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote, open_bar, open_food, estacionamento):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.open_bar:
            print("Pegando uma bebida no open bar.")
        else:
            print("Não há open bar neste ingresso.")

    def acessar_camarote(self):
        if self.camarote:
            print("Acessando o camarote.")
        else:
            print("Este ingresso não dá acesso ao camarote.")