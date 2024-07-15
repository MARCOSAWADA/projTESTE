from Imovel import Imovel

class Apartamento(Imovel):
    def __init__(self, inscricao_Municipal, valor_Aluguel, iptu, area_m2):
        super().__init__(inscricao_Municipal, valor_Aluguel, iptu)
        self.area_m2 = area_m2