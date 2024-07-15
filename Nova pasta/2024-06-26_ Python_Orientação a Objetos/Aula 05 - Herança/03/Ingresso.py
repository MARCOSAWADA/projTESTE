# 3 - Classe Ingresso: Crie uma super classe que modele um Ingresso. Esta classe deve possuir os seguintes atributos:​
# Preco;​
# Setor;​

# Método:​
# alterar_preco() e mostrar_setor();​

# Subclasses:​
# Defina a subclasse ingressoVIP com os seguintes atributos: camarote, open_bar, open_food, estacionamento -> todos booleanos, True ou False;​
# Acrescente os métodos pegar_bebida() e acessar_camarote();​

class Ingresso:
    def __init__ (self, preco, setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def mostrar_setor(self):
        print(f"Setor: {self.setor}")