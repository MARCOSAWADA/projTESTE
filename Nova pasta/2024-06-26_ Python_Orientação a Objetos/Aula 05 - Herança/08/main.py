from Imovel import Imovel
from Casa import Casa
from Condominio import Condominio
from Apartamento import Apartamento
from Terreno import Terreno
from Chacara import Chacara


casa1 = Casa(inscricao_Municipal="C123", valor_Aluguel=2000, iptu=500, piscina=True, sala_de_estar=True, quartos=3)
print(f"Casa IPTU parcela: {casa1.obter_parcela_iptu()}")

apartamento1 = Apartamento(inscricao_Municipal="A456", valor_Aluguel=1500, iptu=400, area_m2=80)
print(f"Apartamento IPTU parcela: {apartamento1.obter_parcela_iptu()}")