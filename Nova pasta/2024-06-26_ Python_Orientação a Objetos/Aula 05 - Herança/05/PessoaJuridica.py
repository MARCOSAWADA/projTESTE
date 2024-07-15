from Pessoa2 import Pessoa2

class PessoaJuridica(Pessoa2):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj

    def vender(self):
        print(f"{self.nome} está vendendo como pessoa jurídica.")