# Classe Passagem: Crie uma super classe que modele uma Passagem. Esta classe deve possuir os seguintes atributos:​
# Preco;​
# Assento;​

# Método:​
# alterar_preco() e escolher_assento();​

# Subclasses:​
# Defina a subclasse PassagemBus e PassagemAviao com os seguintes atributos: portaodeembarque e checkin para classe PassagemAviao, placa e leito par PassagemBus;​
# Crie um novo método específico para cada subclasse. Ex: decolar() e abastecer()​

class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def escolher_assento(self, novo_assento):
        self.assento = novo_assento