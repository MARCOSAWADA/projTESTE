from Passagem import Passagem
from PassagemAviao import PassagemAviao
from PassagemBus import PassagemBus

passagem_bus = PassagemBus(preco=50, assento="12A", placa="ABC123", leito=True)
passagem_bus.abastecer()

passagem_aviao = PassagemAviao(preco=200, assento="5C", portaodeembarque="G5", checkin=True)
passagem_aviao.decolar()