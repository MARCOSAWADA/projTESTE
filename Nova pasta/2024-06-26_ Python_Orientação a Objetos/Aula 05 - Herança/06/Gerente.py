from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha

    def aprovar_folha_pagamento(self):
        print(f"{self.nome} aprovou a folha de pagamento.")