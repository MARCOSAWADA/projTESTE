from Funcionario import Funcionario
from Vendedor import Vendedor
from Gerente import Gerente

vendedor1 = Vendedor(nome="Carlos", matricula="V123", salario=3000, comissao=0.1)
vendedor1.bater_pontos(1)
vendedor1.bater_pontos(0)
vendedor1.bater_meta()

gerente1 = Gerente(nome="Ana", matricula="G456", salario=6000, senha="1234")
gerente1.bater_pontos(1)
gerente1.aprovar_folha_pagamento()
