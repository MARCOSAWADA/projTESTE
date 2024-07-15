from Imovel import Imovel

class Chacara(Imovel):
    def __init__(self, inscricao_Municipal, valor_Aluguel, iptu):
        super().__init__(inscricao_Municipal, valor_Aluguel, iptu)