from Pessoa2 import Pessoa2

class PessoaFisica(Pessoa2):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def comprar(self):
        print(f"{self.nome} está comprando como pessoa física.")