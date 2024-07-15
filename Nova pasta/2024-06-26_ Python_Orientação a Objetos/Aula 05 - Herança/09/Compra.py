# Classe Compra: Crie uma super classe que modele uma Venda. Esta classe deve possuir os seguintes atributos:​
# Numero; Produto; Valor; Valor_total = 0;​

# Método:​
# calcular_valor_total(): deve somar ao valor_total o imposto de 17% do ICMS + o Frete de 5% sobre o valor do protudo;​

# Subclasses:​
# Defina as subclasses Avista e Parcelada, 
# na classe de compra a vista deve ter o atributo desconto e na classe Parcelada numero de parcelas.​
# Em cada subclasse definir um método que retorna o preço com desconto ou o valor das parcelas.​

class Compra:
    def __init__ (self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0

    def calcular_valor_total(self):
        icms = 0.17 * self.valor
        frete = 0.05 * self.valor
        self.valor_total = self.valor + icms + frete
