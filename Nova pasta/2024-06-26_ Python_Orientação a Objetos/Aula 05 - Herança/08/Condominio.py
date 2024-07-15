from Imovel import Imovel

class Condominio(Imovel):
    def __init__(self, inscricao_Municipal, valor_Aluguel, iptu, elevador, area_de_lazer):
        super().__init__(inscricao_Municipal, valor_Aluguel, iptu)
        self.elevador = elevador
        self.area_de_lazer = area_de_lazer