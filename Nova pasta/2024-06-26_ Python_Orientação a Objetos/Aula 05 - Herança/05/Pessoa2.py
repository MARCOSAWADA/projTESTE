# Classe Pessoa: Crie uma super classe que modele uma Pessoa. Esta classe deve possuir os seguintes atributos:​
# Nome; Telefone; E-mail; Endereço;​

# Métodos:​
# negociar: deve printar uma mensagem de negociação;​

# Subclasses:​
# Defina as subclasses de Pessoa serão Física e Jurídica, estas devem conter além dos atributos herdados de Pessoa seus atributos identificadores, ex: CPF, CNPJ.​

# Além de herdar o método negociar() crie métodos específicos para as subclasses;​

class Pessoa2:
    def __init__ (self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"{self.nome} está negociando.")