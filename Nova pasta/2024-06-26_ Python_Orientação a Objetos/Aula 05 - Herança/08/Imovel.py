# Classe Imóvel: Uma Imobiliária precisa de um sistema que controle o aluguel de seus Imóveis. 
# Para isto você deve definir em um módulo a super classe Imóvel com os seguintes atributos:​
# InscricaoMunicipal; Valor_aluguel; IPTU;​

# Método:​
# obter_parcela_IPTU();​
# Set_valor_aluguel();​

# Subclasses:​
# Defina as subclasses de Imóvel sendo: Casa, Condomínio; Apartamento; Terreno e Chácara;​
# Defina os atributos específicos para cada sub classe, exemplo: piscina, sala_de_estar, ​
# Quartos, churrasqueira, área m², elevador, área_de_lazer.​

class Imovel:
    def __init__ (self, inscricaoMunicipal, valor_Aluguel, iptu):
        self.inscricaoMunicipal = inscricaoMunicipal
        self.valor_Aluguel = valor_Aluguel
        self.iptu = iptu

    def obter_parcela_iptu(self):
        return self.iptu / 12
    
    def set_valor_aluguel(self, novo_valor):
        self.valor_aluguel = novo_valor