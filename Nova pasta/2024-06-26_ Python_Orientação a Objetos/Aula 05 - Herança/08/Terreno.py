from Imovel import Imovel

class Terreno(Imovel):
    def __init__(self, inscricao_Municipal, valor_Aluguel, iptu):
        super().__init__(inscricao_Municipal, valor_Aluguel, iptu)