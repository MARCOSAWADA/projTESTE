from Imovel import Imovel

class Casa(Imovel):
    def __init__(self, inscricao_Municipal, valor_Aluguel, iptu, piscina, sala_de_estar, quartos):
        super().__init__(inscricao_Municipal, valor_Aluguel, iptu)
        self.piscina = piscina
        self.sala_de_estar = sala_de_estar
        self.quartos = quartos